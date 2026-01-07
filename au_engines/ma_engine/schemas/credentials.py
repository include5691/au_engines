from typing import Annotated
from pydantic import BaseModel, Field

from au_engines.instances_base.mixins import InstanceIdMixin


class MaChannelCredentialsRequest(BaseModel):

    user_id: Annotated[
        int,
        Field(
            description="User identifier in the system",
            ge=1,
        ),
    ]


class MaChannelCredentialsResponse(MaChannelCredentialsRequest, InstanceIdMixin):

    token: Annotated[
        str,
        Field(
            description="API token for the instance associated with the channel",
            min_length=1,
        ),
    ]
    phone: Annotated[
        str,
        Field(
            description="Phone number associated with the channel",
            min_length=11,
            max_length=11,
        ),
    ]
    name: Annotated[
        str | None,
        Field(
            description="Name of the channel",
            min_length=1,
            max_length=100,
        ),
    ]
    daily_limit: Annotated[
        int,
        Field(
            description="Daily limit of events for the channel",
            ge=0,
        ),
    ]
    toggle_pro: Annotated[
        bool,
        Field(
            description="Flag indicating whether pro events are enabled for the channel",
        ),
    ]
