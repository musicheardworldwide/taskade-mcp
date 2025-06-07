# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .space_agent import SpaceAgent

__all__ = ["FolderGenerateAgentResponse"]


class FolderGenerateAgentResponse(BaseModel):
    item: SpaceAgent

    ok: Literal[True]
