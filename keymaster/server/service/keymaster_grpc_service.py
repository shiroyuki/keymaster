import json
from typing import Optional, Tuple, Any

import grpc

from keymaster.common.proto.keymaster_pb2 import UserAuthenticationResponse
from keymaster.common.proto.keymaster_pb2_grpc import KeymasterServicer


class KeymasterGRPCService(KeymasterServicer):
    def AuthenticateUser(self, request, context):
        return UserAuthenticationResponse(refresh_token='abc')

    def Search(self, request, context):
        self.bail_out(context, dict(foo='bar'), status_code=grpc.StatusCode.PERMISSION_DENIED)

    def bail_out(self, context, details: Optional[Any] = None, status_code: Optional[Tuple[int, str]] = None):
        details_as_json_string = json.dumps(details, sort_keys=True)
        context.set_code(status_code or grpc.StatusCode.INTERNAL)
        context.set_details(details_as_json_string)
        raise BailedOut(details_as_json_string)


class BailedOut(RuntimeError):
    pass
