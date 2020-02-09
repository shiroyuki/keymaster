from dataclasses import asdict

from gallium import ICommand
from imagination import container
import yaml

from keymaster.server.model.user import DefaultRole
from keymaster.server.service.user_service import UserService


class CreateNewUser(ICommand):
    """Create a new user (run as a system user)"""

    def identifier(self):
        return 'user:add'

    def define(self, parser):
        parser.add_argument('--admin',
                            action='store_true',
                            help='Flag to create an admin-level user (higher)',
                            required=False)
        parser.add_argument('--owner',
                            action='store_true',
                            help='Flag to create an owner-level user (highest)',
                            required=False)
        parser.add_argument('--name', '-n',
                            help='The descriptive name of the user (If not given, it will be the same as the username)',
                            required=False)
        parser.add_argument('--username', '-u',
                            help='The username (email) used for authentication',
                            required=True)
        parser.add_argument('--password', '-p',
                            help='The password (If not given, the CLI will automatically generate a secure one)',
                            required=False)

    def execute(self, args):
        role = DefaultRole.USER
        if args.owner and args.admin:
            raise RuntimeError("A user can only be either an admin or an owner, but not both.")
        elif args.owner:
            role = DefaultRole.OWNER
        elif args.admin:
            role = DefaultRole.ADMIN
        us: UserService = container.get(UserService)
        print('Adding a new user...')
        new_user_receipt = us.create(role, args.name, args.username, args.password)
        print('A new user has been registered.\n\n')
        print(yaml.dump(asdict(new_user_receipt), Dumper=yaml.SafeDumper))
