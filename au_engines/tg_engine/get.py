import os
import logging
import requests
from requests.exceptions import RequestException
from au_engines._totp import totp
from .types import TelegramChannel

def get_telegram_channels(user_id: int) -> list[TelegramChannel] | None:
    try:
        with requests.Session() as session:
            response = session.post(
                url=os.getenv("CHC_TELEGRAM_CHANNELS_URL"),
                json={"user_id": user_id},
                headers={"Authorization": totp.now()},
                timeout=10,
            )
            data = response.json()
            if not data or not isinstance(data, dict) or not "channels" in data:
                return None
            return [TelegramChannel(**channel) for channel in data["channels"]]
    except RequestException as e:
        logging.error(f"RequestException: failed to get telegram channels: {e}")
        return None
    except Exception as e:
        logging.error(f"Exception: failed to get telegram channels: {e}")
        return None