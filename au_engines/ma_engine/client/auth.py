from typing_extensions import deprecated

from au_engines.instances_base import InstanceClientBase
from ..schemas import (
    AuthRequest,
    AuthCodeRequest,
    AuthResponse,
    LogoutResponse,
    QrCodeResponse,
)


class MaClientAuth(InstanceClientBase):

    @deprecated("Use get_qr_code instead")
    def request_auth_code(self, request: AuthRequest) -> AuthResponse | None:
        data = self._post(
            endpoint="/waInstance{idInstance}/startAuthorization/{apiTokenInstance}",
            data=request.model_dump(by_alias=True),
        )
        if data is None:
            return None
        return AuthResponse.model_validate(data)

    @deprecated("Use get_qr_code instead")
    def send_auth_code(self, request: AuthCodeRequest) -> AuthResponse | None:
        data = self._post(
            endpoint="/waInstance{idInstance}/sendAuthorizationCode/{apiTokenInstance}",
            data=request.model_dump(by_alias=True),
        )
        if data is None:
            return None
        return AuthResponse.model_validate(data)

    def get_qr_code(self) -> QrCodeResponse | None:
        data = self._get(
            endpoint="/waInstance{idInstance}/qr/{apiTokenInstance}",
        )
        if data is None:
            return None
        return QrCodeResponse.model_validate(data)

    def logout(self) -> LogoutResponse | None:
        data = self._get(
            endpoint="/waInstance{idInstance}/logout/{apiTokenInstance}",
        )
        if data is None:
            return None
        return LogoutResponse.model_validate(data)
