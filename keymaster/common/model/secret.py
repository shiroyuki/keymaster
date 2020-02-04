from abc import ABC


class Secret(ABC):
    @property
    def id(self) -> str:
        return self.uuid

    @property
    def pk(self) -> str:
        return self.name