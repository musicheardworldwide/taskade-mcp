# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .media import Media
from .._models import BaseModel

__all__ = ["MediaRetrieveResponse"]


class MediaRetrieveResponse(BaseModel):
    item: Optional[Media] = None

    ok: Literal[True]
