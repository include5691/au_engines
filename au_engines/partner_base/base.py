from httpx import Client


class PartnerClientBase:

    def __init__(self, partner_token: str, base_url: str) -> None:
        self.partner_token = partner_token
        self.client = Client(base_url=base_url)

    def _post(self, endpoint: str, data: dict) -> dict | None:
        response = self.client.post(
            url=endpoint.format(partnerToken=self.partner_token),
            json=data,
            timeout=10,
        )
        response.raise_for_status()
        return response.json() if response.content else None

    def _get(self, endpoint: str, params: dict | None = None) -> dict | None:
        response = self.client.get(
            url=endpoint.format(partnerToken=self.partner_token),
            params=params,
            timeout=10,
        )
        response.raise_for_status()
        return response.json() if response.content else None
