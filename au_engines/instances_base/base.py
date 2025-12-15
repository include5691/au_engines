import logging
from httpx import Client, RequestError


class InstanceClientBase:

    def __init__(self, instance_id: str, api_token: str, base_url: str, daily_limit: int | None = None) -> None:
        self.instance_id = instance_id
        self.api_token = api_token
        self.client = Client(base_url=base_url)
        self.daily_limit = daily_limit

    def _post(self, endpoint: str, data: dict) -> dict | None:
        try:
            response = self.client.post(
                url=endpoint.format(
                    idInstance=self.instance_id, apiTokenInstance=self.api_token
                ),
                json=data,
                timeout=10,
            )
            response.raise_for_status()
            return response.json() if response.content else None
        except RequestError as e:
            logging.error(
                f"Request error in instances client during POST to {endpoint}: {e}"
            )
            return None

    def _get(self, endpoint: str, params: dict | None = None) -> dict | None:
        try:
            response = self.client.get(
                url=endpoint.format(
                    idInstance=self.instance_id, apiTokenInstance=self.api_token
                ),
                params=params,
                timeout=10,
            )
            response.raise_for_status()
            return response.json() if response.content else None
        except RequestError as e:
            logging.error(
                f"Request error in instances client during GET to {endpoint}: {e}"
            )
            return None
