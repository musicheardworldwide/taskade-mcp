# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .projects.tasks.user import User

__all__ = ["ProjectListMembersResponse"]


class ProjectListMembersResponse(BaseModel):
    items: List[Optional[User]]

    ok: Literal[True]
