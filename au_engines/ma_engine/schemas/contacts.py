from typing import Annotated
from pydantic import Field, BaseModel

from ...instances_base.mixins import PhoneNumberMixin


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
            description="Chat identifier of the contact",
        ),
    ]

    name: Annotated[
        str,
        Field(
            description="Name of the contact",
        ),
    ]

    contact_name: Annotated[
        str,
        Field(
            validation_alias="contactName",
            description="Contact name stored in the address book",
        ),
    ]

    type: Annotated[
        str,
        Field(
            description="Type of the contact",
        ),
    ]

    phone_number: Annotated[
        int,
        Field(
            validation_alias="phoneNumber",
            description="Phone number of the contact",
        ),
    ]
