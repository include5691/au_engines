from typing import Annotated
from pydantic import BaseModel, Field

from ...instances_base.mixins import PhoneNumberMixin, ResponseStatusMixin
from ..enums import AuthorizationFailureReason


class AuthRequest(PhoneNumberMixin): ...


class AuthCodeRequest(BaseModel):

    code: Annotated[
        str,
        Field(
            description="The authorization code received via SMS",
            min_length=6,
            max_length=6,
        ),
    ]


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


class LogoutResponse(BaseModel):

    is_logout: Annotated[
        bool,
        Field(
            description="Result of the instance logout",
            validation_alias="isLogout",
        ),
    ]
