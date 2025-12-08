from typing import Annotated
from pydantic import BaseModel, Field

from au_engines.partner_base import (
    InstanceRenewRequestBase,
    CreateInstanceResponseBase,
    InstancesResponseBase,
    DeleteInstanceResponseBase,
)


class WaInstanceRenewRequest(InstanceRenewRequestBase):

    poll_message_webhook: Annotated[
        bool,
        Field(
            False,
            serialization_alias="pollMessageWebhook",
            description="Enable poll message webhook",
        ),
    ]
    incoming_block_webhook: Annotated[
        bool,
        Field(
            False,
            serialization_alias="incomingBlockWebhook",
            description="Enable incoming block webhook",
        ),
    ]
    incoming_call_webhook: Annotated[
        bool,
        Field(
            False,
            serialization_alias="incomingCallWebhook",
            description="Enable incoming call webhook",
        ),
    ]
    keep_online_status: Annotated[
        bool,
        Field(
            False,
            serialization_alias="keepOnlineStatus",
            description="Keep online status",
        ),
    ]


class WaCreateInstanceResponse(CreateInstanceResponseBase): ...


class WaInstancesResponse(InstancesResponseBase): ...


class WaDeleteInstanceResponse(DeleteInstanceResponseBase): ...
