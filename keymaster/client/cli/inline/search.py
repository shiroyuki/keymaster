from argparse import Namespace
from functools import lru_cache
from typing import List

from imagination import container

from keymaster.client.cli.inline.abc import SubCommand, InlineParser
from keymaster.client.service.databank import Databank
from keymaster.common.model.credential import Credential


class Search(SubCommand):
    """Search for credentials or notes"""
    @lru_cache(maxsize=1)
    def get_aliases(self) -> List[str]:
        return ['search', 's']

    @lru_cache(maxsize=1)
    def get_parser(self) -> InlineParser:
        parser = self._make_parser()
        parser.add_argument('name')
        return parser

    def run(self, args: Namespace):
        entry_name = args.name

        db: Databank = container.get(Databank)
        results = db.find_many('credentials', entry_name) + db.find_many('notes', entry_name)

        if not results:
            print('Nothing found')
            return

        print(f'Found ({len(results)}):')
        for entry in results:
            if isinstance(entry, Credential):
                print(f' - ID: {entry.id:36}\n   Name: {entry.pk}\n   Username: {entry.username}\n')
            else:
                print(f' - ID: {entry.id:36}\n   Name: {entry.pk}\n')
