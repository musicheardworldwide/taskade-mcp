# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .convo import Convo
from ..._models import BaseModel

__all__ = ["ConvoRetrieveResponse"]


class ConvoRetrieveResponse(BaseModel):
    item: Convo

    ok: Literal[True]
