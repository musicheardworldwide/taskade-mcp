# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .project import Project
from .._models import BaseModel

__all__ = ["FolderListProjectsResponse"]


class FolderListProjectsResponse(BaseModel):
    items: List[Optional[Project]]

    ok: Literal[True]
