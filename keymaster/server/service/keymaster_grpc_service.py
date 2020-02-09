import json
from typing import Optional, Tuple, Any

import grpc
from imagination.decorator.service import registered

from keymaster.common.proto.keymaster_pb2 import UserAuthenticationResponse
from keymaster.common.proto.keymaster_pb2_grpc import KeymasterServicer
from keymaster.server.service.user_service import UserService


@registered(auto_wired=True)
class KeymasterGRPCService(KeymasterServicer):
    def __init__(self, user_service: UserService):
        self._user_service = user_service

    def AuthenticateUser(self, request, context):
        # TODO: Authenticate the request with type "client" (offline client)
        refresh_token = self._user_service.authenticate(request.username, request.password)
        if not refresh_token:
            self.bail_out(context, dict(reason='invalid_credential'), grpc.StatusCode.CANCELLED)
        return UserAuthenticationResponse(refresh_token=refresh_token)

    def Search(self, request, context):
        self.bail_out(context, dict(foo='bar'), status_code=grpc.StatusCode.PERMISSION_DENIED)

    def bail_out(self, context, details: Optional[Any] = None, status_code: Optional[Tuple[int, str]] = None):
        details_as_json_string = json.dumps(details, sort_keys=True)
        context.set_code(status_code or grpc.StatusCode.INTERNAL)
        context.set_details(details_as_json_string)
        raise BailedOut(details_as_json_string)


class BailedOut(RuntimeError):
    pass
