import json
import os
import subprocess
from contextlib import contextmanager
from dataclasses import asdict

from imagination.decorator.service import registered

from keymaster.client.service.local_enigma import LocalEnigma
from keymaster.common.model.decrypted_data import DecryptedData
from keymaster.client.static_config import LOCAL_STORAGE_FILEPATH, CONFIG_ROOT_DIR


@registered(auto_wired=True)
class StorageService:
    def __init__(self, enigma: LocalEnigma):
        self.__in_debug_mode = os.getenv('STORAGE_DEBUG') in ['1', 'true']
        self.__enigma = enigma

    def load(self) -> DecryptedData:
        if not os.path.exists(LOCAL_STORAGE_FILEPATH):
            return DecryptedData.make()

        with open(LOCAL_STORAGE_FILEPATH, 'rb') as f:
            content = f.read()

        return DecryptedData.make(json.loads(self.__enigma.decrypt(content)))

    def save(self, content: DecryptedData):
        subprocess.call(['mkdir', '-p', CONFIG_ROOT_DIR])

        content.credentials.sort(key=lambda n: n.name)
        content.notes.sort(key=lambda n: n.name)

        decrypted_data = asdict(content)
        decrypted_json = json.dumps(decrypted_data, sort_keys=True, indent=2 if self.__in_debug_mode else None)

        with open(LOCAL_STORAGE_FILEPATH, 'wb') as f:
            f.write(self.__enigma.encrypt(decrypted_json).encode())

    @contextmanager
    def on_standby(self):
        data = self.load()
        yield data
        self.save(data)