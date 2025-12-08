from typing import Annotated
from pydantic import BaseModel, Field

from au_engines.partner_base import (
    InstanceRenewRequestBase,
    CreateInstanceResponseBase,
    GetInstancesResponseBase,
    DeleteInstanceResponseBase,
)


class MaInstanceRenewRequest(InstanceRenewRequestBase): ...


class MaCreateInstanceResponse(CreateInstanceResponseBase): ...


class MaGetInstancesResponse(GetInstancesResponseBase): ...


class MaDeleteInstanceResponse(DeleteInstanceResponseBase): ...
