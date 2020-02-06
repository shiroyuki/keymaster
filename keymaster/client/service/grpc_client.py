from contextlib import contextmanager
from typing import ContextManager

import grpc

from keymaster_pb2 import UserAuthenticationRequest, UserAuthenticationResponse
from keymaster_pb2_grpc import KeymasterStub


class GRPCClient:
    def __init__(self, host: str, port: int, use_secure_channel: bool):
        self._host = host
        self._port = port
        self._use_secure_channel = use_secure_channel

    @contextmanager
    def connect(self) -> ContextManager[KeymasterStub]:
        address = f'{self._host}:{self._port}'
        channel = grpc.secure_channel(address, None) if self._use_secure_channel else grpc.insecure_channel(address)
        stub = KeymasterStub(channel)
        yield stub
        del stub
        channel.close()

    def authenticate_user(self, username: str, password: str) -> str:
        with self.connect() as stub:
            request = UserAuthenticationRequest(type='client', username=username, password=password)
            response: UserAuthenticationResponse = stub.AuthenticateUser(request)
        return response.jwt