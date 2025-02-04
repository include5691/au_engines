import os
import logging
import requests
from requests.exceptions import RequestException
from pathlib import Path
from pyrogram import Client
from au_engines._totp import totp
from .types import TelegramChannel

TG_API_ID = os.getenv("TG_API_ID")
TG_API_HASH = os.getenv("TG_API_HASH")

def get_telegram_channels(user_id: str | int) -> list[TelegramChannel] | None:
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

def get_telegram_client(*args, id: int | None = None, phone: str | None = None) -> Client | None:
    if args:
        raise ValueError("get_telegram_client() takes keyword arguments only")
    storage_path = Path(__file__).parent / "sessions"
    key = f"{id}{phone}".replace("None", "")
    if not storage_path.exists():
        storage_path.mkdir()
    session_path = storage_path / f"{key}.session"
    if session_path.exists():
        return Client(key, api_id=TG_API_ID, api_hash=TG_API_HASH, phone_number=phone, workdir=storage_path)
    try:
        with requests.Session() as session:
            response = session.post(
                url=os.getenv("CHC_TELEGRAM_SESSIONS_URL"),
                json={"id": id, "phone": phone},
                headers={"Authorization": totp.now()},
                timeout=10,
            )
            if response.status_code != 200:
                return None
            with open(storage_path / f"{key}.session", "wb") as file:
                file.write(response.content)
            return Client(key, api_id=TG_API_ID, api_hash=TG_API_HASH, phone_number=phone, workdir=storage_path)
    except RequestException as e:
        logging.error(f"RequestException: failed to get telegram client: {e}")
        return None
    except Exception as e:
        logging.error(f"Exception: failed to get telegram client: {e}")
        return None