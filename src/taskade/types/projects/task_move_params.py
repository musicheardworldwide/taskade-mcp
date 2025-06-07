# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TaskMoveParams", "Target"]


class TaskMoveParams(TypedDict, total=False):
    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]

    target: Required[Target]


class Target(TypedDict, total=False):
    position: Required[Literal["beforebegin", "afterbegin", "beforeend", "afterend"]]

    task_id: Required[Annotated[str, PropertyInfo(alias="taskId")]]
