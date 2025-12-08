from typing import Annotated
from pydantic import BaseModel, Field

from au_engines.partner_base import (
    InstanceRenewRequestBase,
    CreateInstanceResponseBase,
    GetInstancesResponseBase,
    DeleteInstanceResponseBase,
)


class WaInstanceRenewRequest(InstanceRenewRequestBase):
    """Pydantic schema for instance renewal data in GA Partner."""

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


class WaGetInstancesResponse(GetInstancesResponseBase): ...


class WaDeleteInstanceResponse(DeleteInstanceResponseBase):

    delete_instance_account: Annotated[
        bool,
        Field(
            validation_alias="deleteInstanceAccount",
            description="Instance deletion flag",
        ),
    ]
