from .base import MaxClientBase
from ..schemas import CheckAccountRequest, CheckAccountResponse, GetContactsResponse


class MaxClientContacts(MaxClientBase):

    def check_account(self, request: CheckAccountRequest) -> CheckAccountResponse:
        response = self._post(
            endpoint="/waInstance{idInstance}/checkAccount/{apiTokenInstance}",
            data=request.model_dump(by_alias=True),
        )
        return CheckAccountResponse(**response)

    def get_contacts(self, count: int | None = None) -> list[GetContactsResponse]:
        params = {"count": count} if count is not None else None
        response = self._get(
            endpoint="/waInstance{idInstance}/getContacts/{apiTokenInstance}",
            params=params,
        )
        return [GetContactsResponse(**contact) for contact in response]

