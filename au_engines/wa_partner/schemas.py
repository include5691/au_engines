from typing import Annotated
from pydantic import BaseModel, Field, model_serializer

from .enums import BOOL_MAP


class InstanceRenewData(BaseModel):
    """Pydantic schema for instance renewal data in GA Partner."""

    webhook_url: Annotated[
        str,
        Field(serialization_alias="webhookUrl", description="Webhook URL for instance"),
    ]
    mark_incoming_messages_readed_on_reply: Annotated[
        bool,
        Field(
            False,
            serialization_alias="markIncomingMessagesReadedOnReply",
            description="Mark incoming messages as read on reply",
        ),
    ]
    outgoing_webhook: Annotated[
        bool,
        Field(
            False,
            serialization_alias="outgoingWebhook",
            description="Enable outgoing webhook",
        ),
    ]
    outgoing_message_webhook: Annotated[
        bool,
        Field(
            False,
            serialization_alias="outgoingMessageWebhook",
            description="Enable outgoing message webhook",
        ),
    ]
    outgoing_api_message_webhook: Annotated[
        bool,
        Field(
            False,
            serialization_alias="outgoingAPIMessageWebhook",
            description="Enable outgoing API message webhook",
        ),
    ]
    state_webhook: Annotated[
        bool,
        Field(
            False,
            serialization_alias="stateWebhook",
            description="Enable state webhook",
        ),
    ]
    incoming_webhook: Annotated[
        bool,
        Field(
            False,
            serialization_alias="incomingWebhook",
            description="Enable incoming webhook",
        ),
    ]
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

    @model_serializer(mode="plain")
    def serialize(
        self,
    ) -> dict:
        data = {}
        for name, field in self.model_fields.items():
            value = getattr(self, name)
            key = field.serialization_alias or name
            if isinstance(value, bool):
                data[key] = BOOL_MAP[value]
            else:
                data[key] = value
        return data


class CreateInstanceResponse(BaseModel):

    api_token_instance: Annotated[
        str,
        Field(
            validation_alias="apiTokenInstance",
            description="API token of the account instance",
        ),
    ]
    api_url: Annotated[
        str,
        Field(validation_alias="apiUrl", description="API host link"),
    ]
    id_instance: Annotated[
        int,
        Field(
            validation_alias="idInstance",
            description="Account instance identifier, uint64 type, 10 digits",
        ),
    ]
    media_url: Annotated[
        str,
        Field(
            validation_alias="mediaUrl", description="API host link for sending files"
        ),
    ]
    type_instance: Annotated[
        str,
        Field(
            validation_alias="typeInstance",
            description="Messenger type for instance account: v3 for MAX, whatsapp for WhatsApp",
        ),
    ]
