from gallium import ICommand

from keymaster.client.service.grpc_client import GRPCClient


class Login(ICommand):
    def identifier(self):
        return 'login'

    def define(self, parser):
        parser.add_argument('--non-secure', action='store_true', required=False)
        parser.add_argument('--port', '-p', required=False, type=int, default=443)
        parser.add_argument('host')
        parser.add_argument('username')
        parser.add_argument('password')

    def execute(self, args):
        client = GRPCClient(args.host, args.port, not args.non_secure)
        print(client.authenticate_user(args.username, args.password))