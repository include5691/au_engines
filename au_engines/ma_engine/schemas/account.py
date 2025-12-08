from typing import Annotated
from pydantic import BaseModel, Field

from ...instances_base.schemas import InstanceSettingsBase


class WaAccountSettingsResponse(InstanceSettingsBase):
    
    chat_id: Annotated[
        str,
        Field(
            alias="chatId",
            description="Personal chat identifier in MAX messenger (empty for notAuthorized, blocked, or starting states)"
        ),
    ]
    suspended_until: Annotated[
        int | None,
        Field(
            None,
            alias="suspendedUntil",
            description="Unix timestamp when temporary restrictions end (present when stateInstance is 'suspended')"
        ),
    ]
    history_sync_progress: Annotated[
        int,
        Field(
            alias="historySyncProgress",
            description="Percentage of chat history sync on the instance"
        ),
    ]
