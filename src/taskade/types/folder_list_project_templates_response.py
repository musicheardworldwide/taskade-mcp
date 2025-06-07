# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FolderListProjectTemplatesResponse", "Item"]


class Item(BaseModel):
    id: str

    name: Optional[str] = None


class FolderListProjectTemplatesResponse(BaseModel):
    items: List[Optional[Item]]

    ok: Literal[True]
