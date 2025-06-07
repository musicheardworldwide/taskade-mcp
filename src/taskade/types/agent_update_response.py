# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .space_agent import SpaceAgent

__all__ = ["AgentUpdateResponse"]


class AgentUpdateResponse(BaseModel):
    item: Optional[SpaceAgent] = None

    ok: Literal[True]
