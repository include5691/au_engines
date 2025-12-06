from typing import Annotated
from pydantic import Field, BaseModel

from .mixins import PhoneNumberMixin


class CheckAccountRequest(PhoneNumberMixin):

    force: Annotated[
        bool,
        Field(
            default=False,
            description="Determines whether to ignore cache. Default is false - method uses cached data. When true, ignores cache and sends request directly to MAX server.",
        ),
    ] = False


class CheckAccountResponse(BaseModel):

    exist: Annotated[
        bool,
        Field(description="Flag indicating whether a MAX account exists on the phone number"),
    ]

    chat_id: Annotated[
        str,
        Field(
            description="ChatId of the MAX user on the phone number",
            validation_alias="chatId",
        ),
    ]


class GetContactsResponse(BaseModel):

    chat_id: Annotated[
        str,
        Field(
            validation_alias="chatId",
        ),
    ]

    name: Annotated[
        str,
        Field(),
    ]

    contact_name: Annotated[
        str,
        Field(
            validation_alias="contactName",
        ),
    ]

    type: Annotated[
        str,
        Field(),
    ]

    phone_number: Annotated[
        int,
        Field(
            validation_alias="phoneNumber",
        ),
    ]
