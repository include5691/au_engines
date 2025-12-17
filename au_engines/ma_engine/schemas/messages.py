from typing import Annotated

from pydantic import BaseModel, Field, AliasChoices, field_validator

from ..enums import (
    ChatHistoryDirection,
    ChatHistoryMessageType,
    ChatHistoryStatusMessage,
)


class SendMessageRequest(BaseModel):

    chat_id: Annotated[str, Field(serialization_alias="chatId")]
    message: Annotated[str, Field(max_length=4000)]
    typing_time: Annotated[
        int | None, Field(None, serialization_alias="typingTime", ge=1000, le=20000)
    ]


class SendMessageResponse(BaseModel):

    id_message: Annotated[str, Field(validation_alias="idMessage")]


class GetChatHistoryRequest(BaseModel):

    chat_id: Annotated[str, Field()]
    count: Annotated[int | None, Field(default=100, ge=1)]


class ChatHistoryExtendedTextMessage(BaseModel):

    text: Annotated[str | None, Field(None)]
    description: Annotated[str | None, Field(None)]
    title: Annotated[str | None, Field(None)]
    jpeg_thumbnail: Annotated[str | None, Field(None, validation_alias="jpegThumbnail")]
    forwarding_score: Annotated[
        int | None, Field(None, validation_alias="forwardingScore")
    ]
    is_forwarded: Annotated[bool | None, Field(None, validation_alias="isForwarded")]


class ChatHistoryReaction(BaseModel):

    text: Annotated[str, Field()]


class ChatHistoryMessage(BaseModel):

    type_: Annotated[ChatHistoryDirection, Field(validation_alias="type")]
    id_message: Annotated[str, Field(validation_alias="idMessage")]
    timestamp: Annotated[int, Field()]
    status_message: Annotated[
        ChatHistoryStatusMessage | None,
        Field(None, validation_alias="statusMessage"),
    ]
    send_by_api: Annotated[bool | None, Field(None, validation_alias="sendByApi")]
    message_type: Annotated[
        ChatHistoryMessageType, Field(validation_alias="typeMessage")
    ]
    chat_id: Annotated[str, Field(validation_alias="chatId")]
    sender_id: Annotated[str | None, Field(None, validation_alias="senderId")]
    sender_name: Annotated[str | None, Field(None, validation_alias="senderName")]
    sender_contact_name: Annotated[
        str | None, Field(None, validation_alias="senderContactName")
    ]
    is_forwarded: Annotated[bool | None, Field(None, validation_alias="isForwarded")]
    forwarding_score: Annotated[
        int | None, Field(None, validation_alias="forwardingScore")
    ]
    text_message: Annotated[str | None, Field(None, validation_alias="textMessage")]
    download_url: Annotated[str | None, Field(None, validation_alias="downloadUrl")]
    caption: Annotated[str | None, Field(None)]
    file_name: Annotated[str | None, Field(None, validation_alias="fileName")]
    jpeg_thumbnail: Annotated[str | None, Field(None, validation_alias="jpegThumbnail")]
    mime_type: Annotated[str | None, Field(None, validation_alias="mimeType")]
    is_animated: Annotated[bool | None, Field(None, validation_alias="isAnimated")]
    extended_text_message: Annotated[
        ChatHistoryExtendedTextMessage | None,
        Field(None, validation_alias="extendedTextMessage"),
    ]
    extended_text_message_data: Annotated[
        ChatHistoryReaction | None,
        Field(None, validation_alias="extendedTextMessageData"),
    ]
