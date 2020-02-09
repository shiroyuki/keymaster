import binascii
import hashlib
from functools import lru_cache
from typing import Optional

import keyring
from cryptography.fernet import Fernet


class Enigma:
    def __init__(self, key: Optional[str] = None):
        self.__key = key

    # FIXME Use something like RSA to encrypt/decrypt data
    @property
    @lru_cache(maxsize=1)
    def _key(self) -> bytes:
        if self.__key is not None:
            return self.__key
        stored_key: str = keyring.get_password('com.shiroyuki.keymaster', 'master_enc_key')
        if not stored_key:
            new_key: bytes = Fernet.generate_key()
            keyring.set_password('com.shiroyuki.keymaster', 'master_enc_key', new_key.decode())
            return new_key
        return stored_key.encode()

    @property
    @lru_cache(maxsize=1)
    def _inf(self):
        return Fernet(self._key)

    def decrypt(self, content: bytes) -> str:
        return self._inf.decrypt(content).decode()

    def encrypt(self, content: str) -> str:
        return self._inf.encrypt(content.encode()).decode()

    def hash512(self, content: str, salt: Optional[str] = None) -> str:
        if salt is None:
            m = hashlib.sha512()
            m.update(content)
            return m.hexdigest()

        dk = hashlib.pbkdf2_hmac('sha512', content.encode(), salt.encode(), 100000)
        return binascii.hexlify(dk).decode()
