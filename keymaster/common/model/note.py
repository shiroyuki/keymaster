from dataclasses import dataclass
from time import time
from typing import Optional, List
from uuid import uuid4

from keymaster.common.model.secret import Secret


@dataclass
class Note(Secret):
    uuid: str
    name: str
    content: str
    tags: List[str]
    created_at: float
    updated_at: Optional[float]
    deleted_at: Optional[float]

    @staticmethod
    def make(name: str, content: str, tags: List[str]):
        return Note(uuid=str(uuid4()),
                    name=name,
                    content=content,
                    tags=tags,
                    created_at=time(),
                    updated_at=None,
                    deleted_at=None)