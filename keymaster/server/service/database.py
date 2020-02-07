from functools import lru_cache

from imagination.decorator.config import EnvironmentVariable
from imagination.decorator.service import registered
from xmode.db.core import Core
from xmode.db.sql_generator import MySQL, SqlGenerator


@registered(params=[
    EnvironmentVariable('DB_URL'),
    EnvironmentVariable('DB_NAME'),
])
class Database(Core):
    @property
    @lru_cache(maxsize=1)
    def sql_generator(self) -> SqlGenerator:
        return MySQL()
