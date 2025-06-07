# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProjectListBlocksParams"]


class ProjectListBlocksParams(TypedDict, total=False):
    after: str
    """Parameter for cursor-based pagination.

    Specify task ID to get blocks after it. Do not specify both before and after.
    """

    before: str
    """Parameter for cursor-based pagination.

    Specify task ID to get blocks before it. Do not specify both before and after.
    """

    limit: float
