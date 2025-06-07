# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WorkspaceListResponse", "Item"]


class Item(BaseModel):
    id: str
    """Unique identifier of the workspace or folder.

    An alphanumeric string that is either 16 characters long or 9 characters long
    (the 9-character version may include underscores or hyphens)
    """

    name: str
    """Name of the workspace or folder."""


class WorkspaceListResponse(BaseModel):
    items: List[Optional[Item]]

    ok: Literal[True]
