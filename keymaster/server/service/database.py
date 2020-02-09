from functools import lru_cache

from imagination.decorator.config import EnvironmentVariable, Service, Parameter
from imagination.decorator.service import registered
from xmode.db.core import Core
from xmode.db.doa import DOA
from xmode.db.sql_generator import MySQL, SqlGenerator


@registered(params=[
    EnvironmentVariable('KEYMASTER_DB_URL'),
    EnvironmentVariable('KEYMASTER_DB_NAME'),
])
class Database(Core):
    @property
    @lru_cache(maxsize=1)
    def sql_generator(self) -> SqlGenerator:
        return MySQL()


@registered(params=[Service(Database)])
class DataAccessor(DOA):
    pass
