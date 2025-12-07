from .base import PartnerClientBase
from ..schemas import CreateInstanceResponse, InstanceRenewData


class PartnerClientInstances(PartnerClientBase):

    def create_instance(self, data: InstanceRenewData) -> CreateInstanceResponse | None:
        response = self._post(
            endpoint="/partner/createInstance/{partnerToken}",
            data=data.model_dump(by_alias=True),
        )
        if not response:
            return None
        return CreateInstanceResponse.model_validate(response)
