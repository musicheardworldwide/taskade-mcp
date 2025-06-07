# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["FieldValue"]


class FieldValue(BaseModel):
    field_id: str = FieldInfo(alias="fieldId")

    value: Optional[object] = None
