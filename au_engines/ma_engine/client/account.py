from au_engines.instances_base import InstanceClientBase
from ..schemas import WaAccountSettingsResponse


class MaClientAccount(InstanceClientBase):

    def get_account_settings(self) -> WaAccountSettingsResponse | None:
        data = self._get(
            endpoint="/waInstance{idInstance}/getAccountSettings/{apiTokenInstance}",
        )
        if not data:
            return None
        return WaAccountSettingsResponse.model_validate(data)
