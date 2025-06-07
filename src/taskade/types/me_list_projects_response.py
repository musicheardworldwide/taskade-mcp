# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .project import Project
from .._models import BaseModel

__all__ = ["MeListProjectsResponse"]


class MeListProjectsResponse(BaseModel):
    items: List[Project]

    ok: Literal[True]
