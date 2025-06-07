# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .convo import Convo
from ..._models import BaseModel

__all__ = ["ConvoListResponse"]


class ConvoListResponse(BaseModel):
    items: List[Convo]

    ok: Literal[True]
