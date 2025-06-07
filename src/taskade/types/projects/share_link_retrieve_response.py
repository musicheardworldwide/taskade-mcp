# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .project_share import ProjectShare

__all__ = ["ShareLinkRetrieveResponse"]


class ShareLinkRetrieveResponse(BaseModel):
    item: Optional[ProjectShare] = None
    """The share links of a project"""

    ok: Literal[True]
