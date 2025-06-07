# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .task_note import TaskNote
from ...._models import BaseModel

__all__ = ["NoteRetrieveResponse"]


class NoteRetrieveResponse(BaseModel):
    item: Optional[TaskNote] = None

    ok: bool
