# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WorkspaceCreateProjectParams"]


class WorkspaceCreateProjectParams(TypedDict, total=False):
    content: Required[str]

    content_type: Required[Annotated[Literal["text/markdown"], PropertyInfo(alias="contentType")]]
