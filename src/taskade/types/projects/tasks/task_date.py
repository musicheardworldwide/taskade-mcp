# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["TaskDate"]


class TaskDate(BaseModel):
    date: str

    time: Optional[str] = None

    timezone: Optional[str] = None
