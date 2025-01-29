from pydantic import BaseModel, model_validator

class TelegramChannel(BaseModel):
    id: int
    username: str
    phone: str
    daily_limit: int
    toggle_mail: bool