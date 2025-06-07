# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ...._models import BaseModel
from .field_value import FieldValue

__all__ = ["FieldListResponse"]


class FieldListResponse(BaseModel):
    items: List[FieldValue]

    ok: Literal[True]
