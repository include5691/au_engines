from typing import Annotated
from pydantic import Field

from ..enums import AuthorizationFailureReason
from .mixins import PhoneNumberMixin, ResponseStatusMixin


class AuthRequest(PhoneNumberMixin): ...


class AuthResponseData(ResponseStatusMixin):

    reason: Annotated[
        AuthorizationFailureReason,
        Field(
            description="The reason for the authorization failure",
        ),
    ]
    ready_after: Annotated[
        int | None,
        Field(
            None,
            description="Time in miliseconds after which the user can retry requesting a new code",
            ge=0,
            validation_alias="retryAfter",
        ),
    ]


class AuthResponse(ResponseStatusMixin):

    data: Annotated[
        AuthResponseData,
        Field(
            description="The detailed data about the authorization failure",
        ),
    ]
