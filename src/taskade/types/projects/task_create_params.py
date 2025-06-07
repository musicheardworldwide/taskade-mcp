# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TaskCreateParams", "Task", "TaskUnionMember0", "TaskUnionMember1"]


class TaskCreateParams(TypedDict, total=False):
    tasks: Required[Iterable[Task]]


class TaskUnionMember0(TypedDict, total=False):
    placement: Required[Literal["afterbegin", "beforeend"]]

    content: str

    content_type: Annotated[Literal["text/markdown", "text/plain"], PropertyInfo(alias="contentType")]

    task_id: Annotated[Optional[Literal["null"]], PropertyInfo(alias="taskId")]


class TaskUnionMember1(TypedDict, total=False):
    placement: Required[Literal["beforebegin", "afterbegin", "beforeend", "afterend"]]

    task_id: Required[Annotated[str, PropertyInfo(alias="taskId")]]

    content: str

    content_type: Annotated[Literal["text/markdown", "text/plain"], PropertyInfo(alias="contentType")]


Task: TypeAlias = Union[TaskUnionMember0, TaskUnionMember1]
