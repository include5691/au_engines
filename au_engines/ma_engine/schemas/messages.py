from typing import Annotated

from pydantic import BaseModel, Field, AliasChoices, field_validator

from ..enums import (
    ChatHistoryDirection,
    ChatHistoryMessageType,
    ChatHistoryStatusMessage,
    TypingType,
)


class SendMessageRequest(BaseModel):

    chat_id: Annotated[
        str,
        Field(
            serialization_alias="chatId",
            description="Chat identifier",
        ),
    ]
    message: Annotated[
        str,
        Field(
            max_length=4000,
            description="Text message content. Supports emoji. Maximum 4000 characters",
        ),
    ]
    typing_time: Annotated[
        int | None,
        Field(
            None,
            serialization_alias="typingTime",
            ge=1000,
            le=20000,
            description="Time to show typing notification in chat (milliseconds, 1000-20000)",
        ),
    ]


class SendMessageResponse(BaseModel):

    id_message: Annotated[
        str,
        Field(
            validation_alias="idMessage",
            description="Identifier of the sent message",
        ),
    ]


class SendFileByUrlRequest(BaseModel):

    chat_id: Annotated[
        str,
        Field(
            serialization_alias="chatId",
            description="Chat identifier",
        ),
    ]
    url_file: Annotated[
        str,
        Field(
            serialization_alias="urlFile",
            description="URL of the file to send",
        ),
    ]
    file_name: Annotated[
        str,
        Field(
            serialization_alias="fileName",
            description="File name with extension (UTF-8 without BOM)",
        ),
    ]
    caption: Annotated[
        str | None,
        Field(
            None,
            max_length=4000,
            description="File caption for videos, images, and documents. Maximum 4000 characters",
        ),
    ]
    typing_time: Annotated[
        int | None,
        Field(
            None,
            serialization_alias="typingTime",
            ge=1000,
            le=20000,
            description="Time to show typing notification in chat (milliseconds, 1000-20000)",
        ),
    ]
    typing_type: Annotated[
        TypingType | None,
        Field(
            None,
            serialization_alias="typingType",
            description="Type of typing notification (text, recording, video, image, file)",
        ),
    ]


class GetChatHistoryRequest(BaseModel):

    chat_id: Annotated[
        str,
        Field(
            description="Chat identifier",
            serialization_alias="chatId",
        ),
    ]
    count: Annotated[
        int | None,
        Field(
            default=100,
            ge=1,
            description="Number of messages to retrieve. Default is 100",
        ),
    ]


class ChatHistoryExtendedTextMessage(BaseModel):

    text: Annotated[
        str | None,
        Field(
            None,
            description="Extended message text content",
        ),
    ]
    description: Annotated[
        str | None,
        Field(
            None,
            description="Extended message description",
        ),
    ]
    title: Annotated[
        str | None,
        Field(
            None,
            description="Extended message title",
        ),
    ]
    jpeg_thumbnail: Annotated[
        str | None,
        Field(
            None,
            validation_alias="jpegThumbnail",
            description="JPEG thumbnail of the extended message",
        ),
    ]
    forwarding_score: Annotated[
        int | None,
        Field(
            None,
            validation_alias="forwardingScore",
            description="Number of times the message was forwarded",
        ),
    ]
    is_forwarded: Annotated[
        bool | None,
        Field(
            None,
            validation_alias="isForwarded",
            description="Flag indicating if the message was forwarded",
        ),
    ]


class ChatHistoryReaction(BaseModel):

    text: Annotated[
        str,
        Field(
            description="Reaction emoji text",
        ),
    ]


class ChatHistoryMessage(BaseModel):

    type_: Annotated[
        ChatHistoryDirection,
        Field(
            validation_alias="type",
            description="Message direction (incoming or outgoing)",
        ),
    ]
    id_message: Annotated[
        str,
        Field(
            validation_alias="idMessage",
            description="Message identifier",
        ),
    ]
    timestamp: Annotated[
        int,
        Field(
            description="Unix timestamp of the message",
        ),
    ]
    status_message: Annotated[
        ChatHistoryStatusMessage | None,
        Field(
            None,
            validation_alias="statusMessage",
            description="Message delivery status (sent, delivered, read)",
        ),
    ]
    send_by_api: Annotated[
        bool | None,
        Field(
            None,
            validation_alias="sendByApi",
            description="Flag indicating if the message was sent via API",
        ),
    ]
    message_type: Annotated[
        ChatHistoryMessageType,
        Field(
            validation_alias="typeMessage",
            description="Type of message content",
        ),
    ]
    chat_id: Annotated[
        str,
        Field(
            validation_alias="chatId",
            description="Chat identifier",
        ),
    ]
    sender_id: Annotated[
        str | None,
        Field(
            None,
            validation_alias="senderId",
            description="Sender's user identifier",
        ),
    ]
    sender_name: Annotated[
        str | None,
        Field(
            None,
            validation_alias="senderName",
            description="Sender's display name",
        ),
    ]
    sender_contact_name: Annotated[
        str | None,
        Field(
            None,
            validation_alias="senderContactName",
            description="Sender's contact name in address book",
        ),
    ]
    is_forwarded: Annotated[
        bool | None,
        Field(
            None,
            validation_alias="isForwarded",
            description="Flag indicating if the message was forwarded",
        ),
    ]
    forwarding_score: Annotated[
        int | None,
        Field(
            None,
            validation_alias="forwardingScore",
            description="Number of times the message was forwarded",
        ),
    ]
    text_message: Annotated[
        str | None,
        Field(
            None,
            validation_alias="textMessage",
            description="Text content of the message",
        ),
    ]
    download_url: Annotated[
        str | None,
        Field(
            None,
            validation_alias="downloadUrl",
            description="URL to download media file",
        ),
    ]
    caption: Annotated[
        str | None,
        Field(
            None,
            description="Caption for media files",
        ),
    ]
    file_name: Annotated[
        str | None,
        Field(
            None,
            validation_alias="fileName",
            description="Name of the file attachment",
        ),
    ]
    jpeg_thumbnail: Annotated[
        str | None,
        Field(
            None,
            validation_alias="jpegThumbnail",
            description="JPEG thumbnail of media file",
        ),
    ]
    mime_type: Annotated[
        str | None,
        Field(
            None,
            validation_alias="mimeType",
            description="MIME type of the file",
        ),
    ]
    is_animated: Annotated[
        bool | None,
        Field(
            None,
            validation_alias="isAnimated",
            description="Flag indicating if the media is animated",
        ),
    ]
    extended_text_message: Annotated[
        ChatHistoryExtendedTextMessage | None,
        Field(
            None,
            validation_alias="extendedTextMessage",
            description="Extended text message data",
        ),
    ]
    extended_text_message_data: Annotated[
        ChatHistoryReaction | None,
        Field(
            None,
            validation_alias="extendedTextMessageData",
            description="Reaction data for the message",
        ),
    ]
