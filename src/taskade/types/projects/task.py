# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Task"]


class Task(BaseModel):
    id: str

    completed: Optional[bool] = None

    parent_id: Optional[str] = FieldInfo(alias="parentId", default=None)

    text: Optional[str] = None
