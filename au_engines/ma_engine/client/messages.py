from au_engines.instances_base import InstanceClientBase
from ..schemas import (
    SendMessageRequest,
    SendMessageResponse,
    SendFileByUrlRequest,
    GetChatHistoryRequest,
    ChatHistoryMessage,
)


class MaClientMessages(InstanceClientBase):

    def send_message(self, request: SendMessageRequest) -> SendMessageResponse | None:
        data = self._post(
            endpoint="/waInstance{idInstance}/sendMessage/{apiTokenInstance}",
            data=request.model_dump(by_alias=True, exclude_none=True),
        )
        if data is None:
            return None
        return SendMessageResponse.model_validate(data)

    def send_file_by_url(
        self, request: SendFileByUrlRequest
    ) -> SendMessageResponse | None:
        data = self._post(
            endpoint="/waInstance{idInstance}/sendFileByUrl/{apiTokenInstance}",
            data=request.model_dump(by_alias=True, exclude_none=True),
        )
        if data is None:
            return None
        return SendMessageResponse.model_validate(data)

    def get_chat_history(
        self, request: GetChatHistoryRequest
    ) -> list[ChatHistoryMessage] | None:
        data = self._post(
            endpoint="/waInstance{idInstance}/getChatHistory/{apiTokenInstance}",
            data=request.model_dump(by_alias=True),
        )
        if data is None:
            return None
        return [ChatHistoryMessage.model_validate(message) for message in data]
