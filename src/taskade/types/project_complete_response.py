# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .project import Project
from .._models import BaseModel

__all__ = ["ProjectCompleteResponse"]


class ProjectCompleteResponse(BaseModel):
    item: Optional[Project] = None

    ok: bool
