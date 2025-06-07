# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from .project_share import ProjectShare

__all__ = ["ShareLinkEnableResponse"]


class ShareLinkEnableResponse(BaseModel):
    item: ProjectShare
    """The share links of a project"""

    ok: Literal[True]
