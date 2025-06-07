# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ProjectShare"]


class ProjectShare(BaseModel):
    edit_url: str = FieldInfo(alias="editUrl")

    view_url: str = FieldInfo(alias="viewUrl")

    check_url: Optional[str] = FieldInfo(alias="checkUrl", default=None)
