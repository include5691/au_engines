from enum import StrEnum


class AuthorizationFailureReason(StrEnum):
    ALREADY_REGISTERED = "already_registered"
    VERIFY_CODE_WRONG = "verify_code_wrong"
    CODE_EXPIRED = "code_expired"
    NO_CODE_SENT = "no_code_sent"
    CONNECTION_CLOSED = "connection_closed"
    TIMEOUT = "timeout"
    RATE_LIMIT_EXCEEDED = "rate_limit_exceeded"
    BLOCKED_OR_DELETED = "blocked_or_deleted"
    NO_ERROR = ""


class ChatHistoryDirection(StrEnum):
    INCOMING = "incoming"
    OUTGOING = "outgoing"


class ChatHistoryStatusMessage(StrEnum):
    SENT = "sent"
    DELIVERED = "delivered"
    READ = "read"


class ChatHistoryMessageType(StrEnum):
    TEXT = "textMessage"
    EXTENDED_TEXT = "extendedTextMessage"
    IMAGE = "imageMessage"
    VIDEO = "videoMessage"
    DOCUMENT = "documentMessage"
    AUDIO = "audioMessage"
    REACTION = "reactionMessage"
