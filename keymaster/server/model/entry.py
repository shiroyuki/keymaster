from dataclasses import dataclass
from time import time
from typing import Optional
from uuid import uuid4

from xmode.db.analyzer import stored_in, identified_by, constraint, default
from xmode.db.definitions import UUID, String, Float, Text


@stored_in('entries')
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
    kind: String
    name: String
    searchable_term: String
    content: Text
    created_at: Float
    modified_at: Float
    deleted_at: Optional[Float]
