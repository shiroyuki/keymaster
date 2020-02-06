from dataclasses import dataclass
from datetime import datetime
from time import time
from typing import Optional, Text
from uuid import uuid4

from xmode.db.analyzer import stored_in, identified_by, constraint, default
from xmode.db.definitions import UUID, DateTime


@stored_in('profiles')
@identified_by('id')  # This is a PK.
@constraint('index', ('owner_id',))
@constraint('index', ('owner_id', 'kind',))
@constraint('index', ('owner_id', 'kind', 'name', 'searchable_term',))
@default('id', lambda: str(uuid4()))
@default('created_at', time)
@default('modified_at', time)
@dataclass
class Entry:
    id: UUID
    owner_id: UUID
    kind: str
    name: str
    searchable_term: str
    content: Text
    created_at: float
    modified_at: float
    deleted_at: Optional[float]
