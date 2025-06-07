# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .user import User
from ...._models import BaseModel

__all__ = ["AssigneeListResponse"]


class AssigneeListResponse(BaseModel):
    items: List[User]

    ok: bool
