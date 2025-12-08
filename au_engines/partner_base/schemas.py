from typing import Annotated
from pydantic import BaseModel, Field, model_serializer

from .enums import BOOL_MAP


class InstanceRenewRequestBase(BaseModel):
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


class CreateInstanceResponseBase(BaseModel):

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


class GetInstancesResponseBase(BaseModel):

    id_instance: Annotated[
        int,
        Field(
            validation_alias="idInstance",
            description="Account instance identifier, int64 type, 1 to 10 digits",
        ),
    ]
    name: Annotated[
        str,
        Field(
            description="Instance name specified by user in personal cabinet or via createInstance method",
        ),
    ]
    type_instance: Annotated[
        str,
        Field(
            validation_alias="typeInstance",
            description="Messenger type for instance account",
        ),
    ]
    type_account: Annotated[
        str,
        Field(
            validation_alias="typeAccount",
            description="Not used",
        ),
    ]
    partner_user_uiid: Annotated[
        str,
        Field(
            validation_alias="partnerUserUiid",
            description="Not used",
        ),
    ]
    time_created: Annotated[
        str,
        Field(
            validation_alias="timeCreated",
            description="Instance creation time",
        ),
    ]
    time_deleted: Annotated[
        str,
        Field(
            validation_alias="timeDeleted",
            description="Instance deletion time",
        ),
    ]
    api_token_instance: Annotated[
        str,
        Field(
            validation_alias="apiTokenInstance",
            description="API token of the account instance",
        ),
    ]
    deleted: Annotated[
        bool,
        Field(
            description="Instance state, shows whether instance is deleted or active",
        ),
    ]
    tariff: Annotated[
        str,
        Field(
            description="Connected tariff on the instance",
        ),
    ]
    is_free: Annotated[
        bool,
        Field(
            validation_alias="isFree",
            description="Flag indicates free instance, for example Developer tariff instance",
        ),
    ]
    is_partner: Annotated[
        bool,
        Field(
            validation_alias="isPartner",
            description="Flag indicates whether instance is Partner tariff",
        ),
    ]
    expiration_date: Annotated[
        str,
        Field(
            validation_alias="expirationDate",
            description="Instance expiration date (partner instances are renewed automatically)",
        ),
    ]
    is_expired: Annotated[
        bool,
        Field(
            validation_alias="isExpired",
            description="Instance state, shows whether instance has expired or not",
        ),
    ]


class DeleteInstanceResponseBase(BaseModel):

    delete_instance_account: Annotated[
        bool,
        Field(
            validation_alias="deleteInstanceAccount",
            description="Instance deletion flag",
        ),
    ]
