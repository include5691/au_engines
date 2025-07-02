import logging
import requests
from requests.exceptions import RequestException
from enum import StrEnum

from ._config import Config


class HttpMethod(StrEnum):
    GET = "GET"
    POST = "POST"


class API(Config):

    def call_instance_api(
        self,
        method: str,
        http_method: HttpMethod = HttpMethod.POST,
        payload: dict | None = None,
    ) -> dict | None:
        try:
            with requests.Session() as session:
                url = f"{self.base_url}/waInstance{self.instance_id}/{method}/{self.api_token}"
                if http_method == HttpMethod.GET:
                    response = session.get(url, params=payload, timeout=10)
                else:
                    response = session.post(url, json=payload, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    if data and isinstance(data, dict):
                        return data
        except RequestException as e:
            logging.error(f"RequestException: {method}: {e}")
