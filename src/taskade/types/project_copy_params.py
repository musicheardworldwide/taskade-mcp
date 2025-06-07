# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ProjectCopyParams"]


class ProjectCopyParams(TypedDict, total=False):
    folder_id: Required[Annotated[str, PropertyInfo(alias="folderId")]]

    project_title: Annotated[str, PropertyInfo(alias="projectTitle")]
