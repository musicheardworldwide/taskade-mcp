# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .media import Media
from .._models import BaseModel

__all__ = ["FolderListMediasResponse"]


class FolderListMediasResponse(BaseModel):
    items: List[Optional[Media]]

    ok: Literal[True]
