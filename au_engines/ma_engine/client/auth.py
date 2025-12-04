from .base import MaxClientBase
from ..schemas import AuthRequest, AuthResponse


class MaxClientAuth(MaxClientBase):

    def request_auth_code(self, request: AuthRequest) -> AuthResponse | None:
        data = self._post(
            endpoint="/waInstance{idInstance}/startAuthorization/{apiTokenInstance}",
            data=request.model_dump(by_alias=True),
        )
        if not data:
            return None
        return AuthResponse.model_validate(data)
