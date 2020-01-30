from dataclasses import dataclass
from time import time
from typing import Optional, List
from uuid import uuid4


@dataclass(frozen=True)
class Note:
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