from .base import MaxClientBase
from ..schemas import AuthRequest, AuthCodeRequest, AuthResponse


class MaxClientAuth(MaxClientBase):

    def request_auth_code(self, request: AuthRequest) -> AuthResponse | None:
        data = self._post(
            endpoint="/waInstance{idInstance}/startAuthorization/{apiTokenInstance}",
            data=request.model_dump(by_alias=True),
        )
        if not data:
            return None
        return AuthResponse.model_validate(data)

    def send_auth_code(self, request: AuthCodeRequest) -> AuthResponse | None:
        data = self._post(
            endpoint="/waInstance{idInstance}/sendAuthorizationCode/{apiTokenInstance}",
            data=request.model_dump(by_alias=True),
        )
        if not data:
            return None
        return AuthResponse.model_validate(data)
