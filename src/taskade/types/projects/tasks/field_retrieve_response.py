# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from .field_value import FieldValue

__all__ = ["FieldRetrieveResponse"]


class FieldRetrieveResponse(BaseModel):
    item: FieldValue

    ok: bool
