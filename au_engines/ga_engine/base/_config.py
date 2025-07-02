import os

class Config:

    base_url = os.getenv("GREENAPI_BASE_URL")

    def __init__(self, instance_id: str, api_token: str):
        self.instance_id = instance_id
        self.api_token = api_token