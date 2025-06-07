# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .task import Task
from ..._models import BaseModel

__all__ = ["TaskListResponse"]


class TaskListResponse(BaseModel):
    items: List[Task]

    ok: Literal[True]
