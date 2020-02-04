from argparse import Namespace
from dataclasses import asdict
from functools import lru_cache
from typing import List

import yaml
from imagination import container

from keymaster.client.cli.inline.abc import SubCommand, InlineParser, InlineRuntimeError
from keymaster.client.service.databank import Databank
from keymaster.common.model.secret import Secret


class Get(SubCommand):
    """Get a credential or note - WARNING: Password will be displayed."""

    @lru_cache(maxsize=1)
    def get_aliases(self) -> List[str]:
        return ['get', 'g']

    @lru_cache(maxsize=1)
    def get_parser(self) -> InlineParser:
        parser = self._make_parser()
        parser.add_argument('id')
        return parser

    def run(self, args: Namespace):
        entry_id = args.id

        db: Databank = container.get(Databank)
        entry: Secret = db.get('credentials', entry_id) or db.get('notes', entry_id)

        if not entry:
            raise InlineRuntimeError('Found nothing')

        print('')
        print(yaml.dump(asdict(entry)))
        print('')