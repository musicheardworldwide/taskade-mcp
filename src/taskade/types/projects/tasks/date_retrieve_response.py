# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from .task_date import TaskDate
from ...._models import BaseModel

__all__ = ["DateRetrieveResponse", "Item", "ItemEnd", "ItemEndPeriod"]


class ItemEndPeriod(BaseModel):
    period: str


ItemEnd: TypeAlias = Union[TaskDate, ItemEndPeriod, None]


class Item(BaseModel):
    start: TaskDate

    end: Optional[ItemEnd] = None


class DateRetrieveResponse(BaseModel):
    item: Item

    ok: Literal[True]
