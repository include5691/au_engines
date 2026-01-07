from typing import Annotated
from pydantic import BaseModel, Field, model_validator

class TelegramChannel(BaseModel):
    id: Annotated[int, Field(description="Telegram channel ID")]
    username: Annotated[str | None, Field(None, description="Telegram channel username")]
    phone: Annotated[str, Field(description="Phone number associated with the channel")]
    daily_limit: Annotated[int, Field(description="Daily message limit")]
    toggle_mail: Annotated[bool, Field(description="Toggle mail notifications")]