import json
import sys
from contextlib import contextmanager
from dataclasses import dataclass
from functools import lru_cache
from traceback import print_exc
from typing import ContextManager, Any

import grpc

from keymaster.common.proto.keymaster_pb2 import UserAuthenticationRequest, UserAuthenticationResponse
from keymaster.common.proto.keymaster_pb2_grpc import KeymasterStub


class GRPCClient:
    def __init__(self, host: str, port: int, use_secure_channel: bool):
        self._host = host
        self._port = port
        self._use_secure_channel = use_secure_channel
        self._access_token = None

    @contextmanager
    def connect(self) -> ContextManager[KeymasterStub]:
        address = f'{self._host}:{self._port}'
        channel = grpc.secure_channel(address, None) if self._use_secure_channel else grpc.insecure_channel(address)
        stub = KeymasterStub(channel)
        error = None
        try:
            yield stub
        except Exception as e:
            sys.stderr.write('ERROR: Unexpectedly detected error\n')
            # print_exc()
            error = e
        finally:
            del stub
            channel.close()

        if error:
            raise CallError(ErrorSummary.from_grpc_error(error))

    def authenticate_user(self, username: str, password: str) -> str:
        with self.connect() as stub:
            request = UserAuthenticationRequest(type='client', username=username, password=password)
            response: UserAuthenticationResponse = stub.AuthenticateUser(request)
        return response.refresh_token


@dataclass(frozen=True)
class ErrorSummary:
    code: str
    details: Any
    original: BaseException

    @staticmethod
    def from_grpc_error(e: BaseException):
        if not hasattr(e, 'code') and callable(e.code) and not hasattr(e, 'details') and callable(e.details):
            return ErrorSummary(code=None, details=None, original=e)
        return ErrorSummary(code=e.code(), details=json.loads(e.details()), original=e)


class CallError(RuntimeError):
    pass
