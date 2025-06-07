# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["MeListProjectsParams"]


class MeListProjectsParams(TypedDict, total=False):
    limit: float

    page: float

    sort: Literal["viewed-asc", "viewed-desc"]
