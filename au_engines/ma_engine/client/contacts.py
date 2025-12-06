from .base import MaxClientBase
from ..schemas import CheckAccountRequest, CheckAccountResponse


class MaxClientContacts(MaxClientBase):

    def check_account(self, request: CheckAccountRequest) -> CheckAccountResponse:
        response = self._post(
            endpoint="/waInstance{idInstance}/checkAccount/{apiTokenInstance}",
            data=request.model_dump(by_alias=True),
        )
        return CheckAccountResponse(**response)

