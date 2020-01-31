from argparse import Namespace
from functools import lru_cache
from typing import List

import pyperclip
from imagination import container

from keymaster.cli.kms.inline.abc import SubCommand, InlineParser, InlineRuntimeError
from keymaster.databank import Databank
from keymaster.model.credential import Credential


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

        if not entry:
            raise InlineRuntimeError('Copy nothing to the clipboard')

        for pn in ('uuid', 'name', 'tags'):
            print(f'{pn.upper()}: {getattr(entry, pn) or "<null>"}')

        pyperclip.copy(entry.password)
        print('The password has been copied to your clipboard.')
