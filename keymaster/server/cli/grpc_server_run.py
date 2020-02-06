from concurrent.futures.thread import ThreadPoolExecutor

import grpc
from gallium import ICommand
from gallium.interface import alias
from imagination import container

from keymaster_pb2_grpc import add_KeymasterServicer_to_server
from keymaster.server.service.keymaster_grpc_service import KeymasterGRPCService


@alias('serve')
class GRPCServerRun(ICommand):
    """Run the gRPC server"""

    def identifier(self):
        return 'grpc:server:run'

    def define(self, parser):
        parser.add_argument('--port', '-p', type=int, required=False, default=8000)

    def execute(self, args):
        service = KeymasterGRPCService()
        server = grpc.server(ThreadPoolExecutor(max_workers=10))

        add_KeymasterServicer_to_server(service, server)

        server.add_insecure_port(f'[::]:{args.port}')
        server.start()

        print(f'Listening on port {args.port}...')

        try:
            while True: pass
        except KeyboardInterrupt:
            print('Service terminated')
        finally:
            server.stop()
