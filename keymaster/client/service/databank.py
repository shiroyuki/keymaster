from typing import List

from imagination.decorator.service import registered

from keymaster.common.model.secret import Secret
from keymaster.client.service.storage import StorageService


@registered(auto_wired=True)
class Databank:
    def __init__(self, storage: StorageService):
        self.__storage = storage

    def get(self, type: str, id: str) -> Secret:
        data = self.__storage.load()
        if not hasattr(data, type):
            raise UnknownSecretType(type)
        for item in getattr(data, type):
            if item.id == id:
                return item
        return None

    def all_of(self, type: str):
        data = self.__storage.load()
        if not hasattr(data, type):
            raise UnknownSecretType(type)
        return [
            item
            for item in getattr(data, type)
        ]

    def find_many(self, type: str, name: str) -> List[Secret]:
        data = self.__storage.load()
        if not hasattr(data, type):
            raise UnknownSecretType(type)
        return [
            item
            for item in getattr(data, type)
            if name.lower() in item.pk.lower()
        ]


class UnknownSecretType(RuntimeError):
    pass
