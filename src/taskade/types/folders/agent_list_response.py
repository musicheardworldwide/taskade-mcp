# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..space_agent import SpaceAgent

__all__ = ["AgentListResponse"]


class AgentListResponse(BaseModel):
    items: List[Optional[SpaceAgent]]

    ok: Literal[True]
