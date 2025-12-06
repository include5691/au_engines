from typing import Annotated
from pydantic import BaseModel, Field, field_validator


class PhoneNumberMixin(BaseModel):

    phone_number: Annotated[
        int,
        Field(
            description="The phone number in international format: 11 or 12 digits",
            ge=70000000000,
            le=79999999999,
            serialization_alias="phoneNumber",
        ),
    ]


class ResponseStatusMixin(BaseModel):

    status: Annotated[
        bool, Field(description="Indicates whether the request was successful or not")
    ]

    @field_validator("status", mode="before")
    @classmethod
    def parse_status(cls, v: bool | str) -> bool:
        if isinstance(v, str):
            return v.lower() != "fail"
        return v
