from au_engines.partner_base import PartnerClientBase
from ..schemas import (
    WaCreateInstanceResponse,
    WaDeleteInstanceResponse,
    WaGetInstancesResponse,
    WaInstanceRenewRequest,
)


class PartnerClientInstances(PartnerClientBase):

    def create_instance(self, data: WaInstanceRenewRequest) -> WaCreateInstanceResponse | None:
        response = self._post(
            endpoint="/partner/createInstance/{partnerToken}",
            data=data.model_dump(by_alias=True),
        )
        if not response:
            return None
        return WaCreateInstanceResponse.model_validate(response)

    def get_instances(self, only_active: bool = True) -> list[WaGetInstancesResponse] | None:
        response = self._get(
            endpoint="/partner/getInstances/{partnerToken}",
        )
        if not response:
            return None
        result = []
        for instance in response:
            instance_model = WaGetInstancesResponse.model_validate(instance)
            if only_active and instance_model.deleted:
                continue
            result.append(instance_model)
        return result

    def delete_instance(self, id_instance: int) -> WaDeleteInstanceResponse | None:
        response = self._post(
            endpoint="/partner/deleteInstanceAccount/{partnerToken}",
            data={"idInstance": id_instance},
        )
        if not response:
            return None
        return WaDeleteInstanceResponse.model_validate(response)
