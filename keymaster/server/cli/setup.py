from gallium import ICommand
from imagination import container

from keymaster.server.model.entry import Entry
from keymaster.server.model.offline_client import OfflineClient
from keymaster.server.model.tag import Tag
from keymaster.server.model.user import User
from keymaster.server.service.database import Database


class SetUp(ICommand):
    """Set up the server"""

    def identifier(self):
        return 'server:setup'

    def define(self, parser):
        pass

    def execute(self, args):
        db: Database = container.get(Database)
        db.initialize(Entry, OfflineClient, Tag, User)


class TearDown(ICommand):
    """Revert the server setup"""

    def identifier(self):
        return 'server:teardown'

    def define(self, parser):
        pass

    def execute(self, args):
        db: Database = container.get(Database)
        db.deinitialize()
