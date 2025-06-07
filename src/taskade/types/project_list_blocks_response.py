# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ProjectListBlocksResponse", "Item"]


class Item(BaseModel):
    id: str

    completed: Optional[bool] = None

    text: Optional[str] = None


class ProjectListBlocksResponse(BaseModel):
    items: List[Item]

    ok: Literal[True]
