from typing import Annotated
from pydantic import BaseModel, Field

from .enums import InstanceState


class InstanceSettingsBase(BaseModel):
    avatar: Annotated[
        str,
        Field(
            description="Link to messenger account avatar (empty for notAuthorized, blocked, or starting states)"
        ),
    ]
    phone: Annotated[
        str,
        Field(
            description="Messenger account phone number (empty for notAuthorized, blocked, or starting states)"
        ),
    ]
    state_instance: Annotated[
        InstanceState,
        Field(
            alias="stateInstance", description="Instance state"
        ),
    ]
