from dataclasses import dataclass
from uuid import uuid4

from xmode.db.analyzer import default, constraint, identified_by, stored_in
from xmode.db.definitions import UUID, String


@stored_in('entry_tags')
@identified_by('id')  # This is a PK.
@constraint('index', ('owner_id',))
@constraint('unique', ('owner_id', 'entry_id',))
@constraint('unique', ('owner_id', 'name',))
@default('id', lambda: str(uuid4()))
@dataclass
class EntryTag:
    id: UUID
    owner_id: UUID
    entry_id: UUID
    name: String
