from au_engines.instances_base import InstanceClientBase
from ..schemas import GetChatHistoryRequest, ChatHistoryMessage


class MaClientMessages(InstanceClientBase):

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
