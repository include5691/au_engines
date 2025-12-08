from typing import Annotated
from pydantic import BaseModel, Field

from au_engines.partner_base import (
    InstanceRenewRequestBase,
    CreateInstanceResponseBase,
    InstancesResponseBase,
    DeleteInstanceResponseBase,
)


class MaInstanceRenewRequest(InstanceRenewRequestBase): ...


class MaCreateInstanceResponse(CreateInstanceResponseBase): ...


class MaInstancesResponse(InstancesResponseBase): ...


class MaDeleteInstanceResponse(DeleteInstanceResponseBase): ...
