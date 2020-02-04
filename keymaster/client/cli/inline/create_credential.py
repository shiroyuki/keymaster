from argparse import Namespace

from imagination import container

from keymaster.client.cli.inline.abc import SubCommand, InlineParser, List
from keymaster.client.service.storage import StorageService
from keymaster.common.model.credential import Credential


class CreateCredential(SubCommand):
    """Create a new credential"""
    def get_aliases(self) -> List:
        return ['create_credential', 'cc']

    def get_parser(self) -> InlineParser:
        parser = self._make_parser()

        parser.add_argument('--entry-name', '-n', metavar='name')
        parser.add_argument('--username', '-u')
        parser.add_argument('--password', '-p',)
        parser.add_argument('--tags', '-t', metavar='tag', nargs='*', required=False)
        parser.add_argument('--extra', required=False, help="Extra notes")

        return parser

    def run(self, args: Namespace):
        storage: StorageService = container.get(StorageService)

        with storage.on_standby() as data:
            data.credentials.append(Credential.make(args.entry_name,
                                                    args.username,
                                                    args.password,
                                                    args.extra or None,
                                                    args.tags or []))
