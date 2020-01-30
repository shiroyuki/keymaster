import json
import os
from dataclasses import asdict

from imagination.decorator.service import registered

from keymaster.enigma import Enigma
from keymaster.model.decrypted_data import DecryptedData


@registered(auto_wired=True)
class StorageService:
    def __init__(self, enigma: Enigma):
        self.__in_debug_mode = os.getenv('STORAGE_DEBUG') in ['1', 'true']
        self.__enigma = enigma

    def save(self, content: DecryptedData):
        content.credentials.sort(key=lambda n: n.name)
        content.notes.sort(key=lambda n: n.name)

        decrypted_data = asdict(content)
        decrypted_json = json.dumps(decrypted_data, sort_keys=True, indent=2 if self.__in_debug_mode else None)

        print(f'decrypted_json:\n{decrypted_json}\n')
        print(f'encrypted_json:\n{self.__enigma.encrypt(decrypted_json)}\n')
