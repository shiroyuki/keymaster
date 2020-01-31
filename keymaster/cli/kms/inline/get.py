from argparse import Namespace
from dataclasses import asdict
from functools import lru_cache
from typing import List

import yaml
from imagination import container

from keymaster.cli.kms.inline.abc import SubCommand, InlineParser, InlineRuntimeError
from keymaster.databank import Databank
from keymaster.model.secret import Secret


class Get(SubCommand):
    """Get a credential (c) or note (n) - WARNING: Password will be displayed."""
    _type_aliases = {
        'c': 'credentials',
        'n': 'notes',
    }

    @lru_cache(maxsize=1)
    def get_aliases(self) -> List[str]:
        return ['get', 'g']

    @lru_cache(maxsize=1)
    def get_parser(self) -> InlineParser:
        parser = self._make_parser()
        parser.add_argument('type')
        parser.add_argument('id')
        return parser

    def run(self, args: Namespace):
        entry_type = args.type
        entry_id = args.id

        db: Databank = container.get(Databank)
        entry: Secret = db.get(self._type_aliases.get(entry_type) or entry_type, entry_id)

        if not entry:
            raise InlineRuntimeError('Found nothing')

        print('')
        print(yaml.dump(asdict(entry)))
        print('')