class Utils:

    @staticmethod
    def phone_encode(phone: str) -> str:
        return str(phone) + "@c.us"

    @staticmethod
    def phone_decode(chatId: str) -> str:
        return chatId.split("@")[0]
