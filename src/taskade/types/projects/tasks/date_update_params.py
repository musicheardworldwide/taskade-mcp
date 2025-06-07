# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from .task_date_param import TaskDateParam

__all__ = ["DateUpdateParams"]


class DateUpdateParams(TypedDict, total=False):
    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]

    start: Required[TaskDateParam]

    end: TaskDateParam
