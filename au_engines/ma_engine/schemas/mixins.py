from typing import Annotated
from pydantic import BaseModel, Field, field_validator


class PhoneNumberMixin(BaseModel):

    phone_number: Annotated[
        str,
        Field(
            description="The phone number in international format without '+' sign",
            max_length=11,
            min_length=11,
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
