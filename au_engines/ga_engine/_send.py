from .base import Base

class Send(Base):

    def send_text(self, phone: str, text: str) -> str | None:
        data = self.call_instance_api("sendMessage", {"chatId": self.phone_encode(phone), "message": text})
        if not data:
            return None
        message_id = data.get("idMessage")
        if message_id:
            return message_id

    def send_poll(self, phone: str, text: str, options: list[str]) -> str | None:
        data = self.call_instance_api("sendPoll", {"chatId": self.phone_encode(phone), "message": text[:255], "options": [{"optionName": option} for option in options[:12]]})
        if not data:
            return None
        message_id = data.get("idMessage")
        if message_id:
            return message_id