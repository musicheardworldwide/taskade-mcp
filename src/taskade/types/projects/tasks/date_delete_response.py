# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..task import Task
from ...._models import BaseModel

__all__ = ["DateDeleteResponse"]


class DateDeleteResponse(BaseModel):
    item: Optional[Task] = None

    ok: Literal[True]
