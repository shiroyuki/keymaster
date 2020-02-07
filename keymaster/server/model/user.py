from dataclasses import dataclass
from time import time
from typing import Optional
from uuid import uuid4

from xmode.db.analyzer import default, constraint, identified_by, stored_in
from xmode.db.definitions import UUID, Float, String


@stored_in('offline_clients')
@identified_by('id')  # This is a PK.
@constraint('index', ('owner_id',))
@constraint('index', ('owner_id', 'kind',))
@constraint('index', ('owner_id', 'kind', 'name', 'searchable_term',))
@default('id', lambda: str(uuid4()))
@default('created_at', time)
@default('modified_at', time)
@dataclass
class User:
    id: UUID

    remote_id: UUID
    # The remote ID is a UUID3 ID based on the client's hostname.
    # We use this to ensure that the data is not duplicated and
    # used on the different machine without proper re-authorization.

    owner_id: UUID
    kind: String  # e.g., cli, desktop/macos, mobile/ios
    name: String
    status: String
    created_at: Float
    modified_at: Float
    deleted_at: Optional[Float]


class ClientStatus:
    ACTIVE = 'active'
    DISABLED = 'disabled'
    BLOCKED = 'blocked'
