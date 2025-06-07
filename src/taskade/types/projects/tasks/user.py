# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["User"]


class User(BaseModel):
    handle: str

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
