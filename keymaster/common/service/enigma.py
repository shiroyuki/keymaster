from functools import lru_cache

import keyring
from cryptography.fernet import Fernet
from imagination.decorator.service import registered


@registered()
class Enigma:
    # FIXME Use something like RSA to encrypt/decrypt data
    @property
    @lru_cache(maxsize=1)
    def _key(self) -> bytes:
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
