# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .project import Project
from .._models import BaseModel

__all__ = ["WorkspaceCreateProjectResponse"]


class WorkspaceCreateProjectResponse(BaseModel):
    item: Project

    ok: Literal[True]
