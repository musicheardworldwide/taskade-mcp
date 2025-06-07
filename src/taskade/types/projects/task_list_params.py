# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TaskListParams"]


class TaskListParams(TypedDict, total=False):
    after: str
    """Parameter for cursor-based pagination.

    Specify task ID to get tasks after it. Do not specify both before and after.
    """

    before: str
    """Parameter for cursor-based pagination.

    Specify task ID to get tasks before it. Do not specify both before and after.
    """

    limit: float
