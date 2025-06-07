# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TaskUpdateParams"]


class TaskUpdateParams(TypedDict, total=False):
    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]

    content: Required[str]

    content_type: Required[Annotated[Literal["text/markdown", "text/plain"], PropertyInfo(alias="contentType")]]
