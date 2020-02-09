from dataclasses import dataclass
from time import time
from typing import Optional
from uuid import uuid4

from xmode.db.analyzer import default, constraint, identified_by, stored_in
from xmode.db.definitions import UUID, Float, String, Text


@stored_in('users')
@identified_by('id')  # This is a PK.
@constraint('unique', 'username')
@default('id', lambda: str(uuid4()))
@default('created_at', time)
@default('modified_at', time)
@dataclass
class User:
    id: UUID
    default_role: String  # e.g., admin, user
    name: String
    username: String
    password: Text
    password_salt: Text
    status: String
    created_at: Float
    modified_at: Float
    deleted_at: Optional[Float]


class Status:
    ACTIVE = 'active'
    DISABLED = 'disabled'
    BLOCKED = 'blocked'


class DefaultRole:
    OWNER = 'owner'
    ADMIN = 'admin'
    USER = 'user'
