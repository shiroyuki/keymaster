from dataclasses import dataclass
from time import time
from typing import Optional, List
from uuid import uuid4

from keymaster.common.model.secret import Secret


@dataclass
class Credential(Secret):
    uuid: str
    name: str
    username: str
    password: str
    content: Optional[str]
    tags: List[str]
    created_at: float
    updated_at: float
    deleted_at: Optional[float]

    @staticmethod
    def make(name: str, username: str, password: str, content: Optional[str], tags: List[str]):
        return Credential(uuid=str(uuid4()),
                          name=name,
                          content=content,
                          tags=tags,
                          username=username,
                          password=password,
                          created_at=time(),
                          updated_at=None,
                          deleted_at=None)
