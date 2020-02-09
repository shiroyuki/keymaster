from datetime import timedelta
from time import time
from typing import Optional, Dict, Any, List

from imagination.decorator.config import EnvironmentVariable
from imagination.decorator.service import registered
import jwt


@registered(params=[
    EnvironmentVariable('KEYMASTER_JWT_SECRET'),
    EnvironmentVariable('KEYMASTER_JWT_ISSUER'),
    EnvironmentVariable('KEYMASTER_JWT_AUDIENCE'),
])
class JWTService:
    def __init__(self, secret: str, issuer: str, audience: str):
        self.__algorithm = 'HS512'
        self.__secret = secret
        self.__issuer = issuer
        self.__audience = audience

    def encode(self, claims: Dict[str, Any], scope: Optional[List[str]] = None, ttl: Optional[int] = None) -> str:
        claims['aud'] = self.__audience
        claims['iss'] = self.__issuer
        claims['iat'] = time()

        if ttl is not None:
            claims['exp'] = claims['iat'] + ttl

        if scope:
            claims['scope'] = scope

        return jwt.encode(claims, self.__secret, self.__algorithm).decode()

    def decode(self, token: str, scope: Optional[List[str]] = None) -> Dict[str, Any]:
        try:
            claims = jwt.decode(token,
                                self.__secret,
                                leeway=timedelta(seconds=10),
                                algorithms=[self.__algorithm])
        except jwt.InvalidTokenError as e:
            raise TokenValidationError(token, e)

        if scope is not None:
            expected_scope_set = set(scope)
            provided_scope_set = expected_scope_set.intersection(claims['scope'])
            if len(provided_scope_set) > len(scope):
                raise InsufficientPermissionError(expected_scope_set.difference(provided_scope_set))

        return claims


class TokenValidationError(RuntimeError):
    pass


class InsufficientPermissionError(RuntimeError):
    pass
