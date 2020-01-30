from dataclasses import dataclass
from time import time
from typing import Optional, List
from uuid import uuid4


@dataclass(frozen=True)
class Credential:
    uuid: str
    name: str
    username: str
    password: str
    extra: str
    tags: List[str]
    created_at: float
    updated_at: float
    deleted_at: Optional[float]

    @staticmethod
    def make(name: str, username: str, password: str, extra: str, tags: List[str]):
        return Credential(uuid=str(uuid4()),
                          name=name,
                          username=username,
                          password=password,
                          extra=extra,
                          tags=tags,
                          created_at=time(),
                          updated_at=None,
                          deleted_at=None)
