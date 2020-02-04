from argparse import Namespace
from functools import lru_cache
from typing import List

import pyperclip
from imagination import container

from keymaster.client.cli.inline.abc import SubCommand, InlineParser, InlineRuntimeError
from keymaster.client.service.databank import Databank
from keymaster.common.model.credential import Credential
from keymaster.common.model.note import Note


class CopyPassword(SubCommand):
    """Search for credentials (c) or notes (n)"""

    @lru_cache(maxsize=1)
    def get_aliases(self) -> List[str]:
        return ['copy-password', 'cp']

    @lru_cache(maxsize=1)
    def get_parser(self) -> InlineParser:
        parser = self._make_parser()
        parser.add_argument('id')
        return parser

    def run(self, args: Namespace):
        db: Databank = container.get(Databank)
        entry: Credential = db.get('credentials', args.id)

        if isinstance(entry, Note):
            raise InlineRuntimeError('The request ID is not a credential.')

        if not entry:
            print('The requested ID does not exist.')
            return

        for pn in ('uuid', 'name', 'tags'):
            print(f'{pn.upper()}: {getattr(entry, pn) or "<null>"}')

        pyperclip.copy(entry.password)
        print('The password has been copied to your clipboard.')
