from keymaster_pb2 import UserAuthenticationResponse
from keymaster_pb2_grpc import KeymasterServicer


class KeymasterGRPCService(KeymasterServicer):
    def AuthenticateUser(self, request, context):
        return UserAuthenticationResponse(jwt='abc')
