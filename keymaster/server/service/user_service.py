from dataclasses import dataclass
from typing import Optional

from imagination.decorator.service import registered
from sqlalchemy.exc import IntegrityError

from keymaster.common.service.randomizer import Randomizer, RandomizerMethod
from keymaster.server.model.user import User, Status
from keymaster.server.service.database import DataAccessor
from keymaster.server.service.jwt_service import JWTService
from keymaster.server.service.server_enigma import ServerEnigma


@dataclass
class NewUserReceipt:
    user: User
    plain_password: str


@registered(auto_wired=True)
class UserService:
    MIN_PLAIN_PASSWORD_LENGTH = 6
    MAX_PLAIN_PASSWORD_LENGTH = 80

    def __init__(self, accessor: DataAccessor, cryptographer: ServerEnigma, randomizer: Randomizer, jwt: JWTService):
        self.__accessor = accessor
        self.__cryptographer = cryptographer
        self.__randomizer = randomizer
        self.__jwt = jwt

    def create(self,
               default_role: str,
               name: Optional[str],
               username: str,
               plain_password: Optional[str]) -> NewUserReceipt:
        if not plain_password:
            plain_password = self.__randomizer.randomize(RandomizerMethod.OPENSSL_HEX, 12)

        self._check_for_password_compliance(plain_password)

        password_salt = self.__randomizer.randomize(RandomizerMethod.OPENSSL_HEX, 32)
        encoded_password = self.__cryptographer.hash512(plain_password, password_salt)

        try:
            existing_user = self.find_one_by_username(username)
            if existing_user:
                raise UserAlreadyExistedError(username)
            user = self.__accessor.create(User,
                                          dict(default_role=default_role,
                                               name=name or username,
                                               username=username,
                                               password=self.__cryptographer.encrypt(encoded_password),
                                               password_salt=self.__cryptographer.encrypt(password_salt),
                                               status=Status.ACTIVE),
                                          return_nothing=False)

            return NewUserReceipt(user=user, plain_password=plain_password)
        except IntegrityError as e:
            if 'Duplicate entry' in e.args:
                raise UserAlreadyExistedError(username)
            else:
                raise UserCreationError(username)

    def authenticate(self, username: str, plain_password: str) -> Optional[str]:
        self._check_for_password_compliance(plain_password)

        user = self.find_one_by_username(username)

        if not user:
            return None

        decrypted_password_salt = self.__cryptographer.decrypt(user.password_salt.encode())
        decrypted_password = self.__cryptographer.decrypt(user.password.encode())
        given_encoded_password = self.__cryptographer.hash512(plain_password, decrypted_password_salt)

        if decrypted_password != given_encoded_password:
            return None

        return self.__jwt.encode(dict(sub=user.id), ['refresh_token'], ttl=30)

    def find_one_by_username(self, username: str) -> User:
        try:
            return list(self.__accessor.find(User, 'username = :username', dict(username=username)))[0]
        except IndexError:
            return None

    def _check_for_password_compliance(self, plain_password: str):
        plain_password_length = len(plain_password)
        if plain_password_length < self.MIN_PLAIN_PASSWORD_LENGTH:
            exceeded_length = self.MIN_PLAIN_PASSWORD_LENGTH - plain_password_length
            raise ForbiddenPasswordError(f'The given password is shorter than the limit by {exceeded_length} character(s).')
        if plain_password_length > self.MAX_PLAIN_PASSWORD_LENGTH:
            exceeded_length = plain_password_length - self.MAX_PLAIN_PASSWORD_LENGTH
            raise ForbiddenPasswordError(f'The given password exceeds the limit by {exceeded_length} character(s).')


class UserCreationError(RuntimeError):
    pass


class UserAlreadyExistedError(UserCreationError):
    pass


class ForbiddenPasswordError(RuntimeError):
    pass
