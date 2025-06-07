# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ProjectListFieldsResponse",
    "Item",
    "ItemData",
    "ItemDataType",
    "ItemDataUnionMember3",
    "ItemDataUnionMember4",
    "ItemDataUnionMember5",
    "ItemDataUnionMember5Options",
    "ItemDataUnionMember6",
    "ItemDataUnionMember6Format",
    "ItemDataUnionMember6FormatType",
    "ItemDataUnionMember6FormatUnionMember1",
    "ItemDataUnionMember6FormatUnionMember1Config",
    "ItemDataUnionMember6FormatUnionMember2",
    "ItemDataUnionMember6FormatUnionMember2Config",
    "ItemDataUnionMember6Render",
    "ItemDataUnionMember7",
    "ItemDataUnionMember8",
    "ItemDataUnionMember9",
    "ItemDataUnionMember9Format",
    "ItemDataUnionMember10",
    "ItemDataUnionMember10Format",
]


class ItemDataType(BaseModel):
    type: Literal["boolean"]


class ItemDataUnionMember3(BaseModel):
    type: Literal["TimestampAt"]

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)


class ItemDataUnionMember4(BaseModel):
    type: Literal["TimestampAuthor"]

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)


class ItemDataUnionMember5Options(BaseModel):
    id: str

    name: str

    rank: str

    color: Optional[str] = None

    description: Optional[str] = None


class ItemDataUnionMember5(BaseModel):
    display_name: str = FieldInfo(alias="displayName")

    options: Dict[str, ItemDataUnionMember5Options]

    type: Literal["Select"]

    default_option: Optional[str] = FieldInfo(alias="defaultOption", default=None)

    description: Optional[str] = None


class ItemDataUnionMember6FormatType(BaseModel):
    type: Literal["decimal"]


class ItemDataUnionMember6FormatUnionMember1Config(BaseModel):
    code: str

    type: Literal["standard"]


class ItemDataUnionMember6FormatUnionMember1(BaseModel):
    config: ItemDataUnionMember6FormatUnionMember1Config

    type: Literal["currency"]


class ItemDataUnionMember6FormatUnionMember2Config(BaseModel):
    type: Literal["standard"]

    unit: str


class ItemDataUnionMember6FormatUnionMember2(BaseModel):
    config: ItemDataUnionMember6FormatUnionMember2Config

    type: Literal["unit"]


ItemDataUnionMember6Format: TypeAlias = Union[
    ItemDataUnionMember6FormatType, ItemDataUnionMember6FormatUnionMember1, ItemDataUnionMember6FormatUnionMember2
]


class ItemDataUnionMember6Render(BaseModel):
    type: Literal["text"]


class ItemDataUnionMember6(BaseModel):
    display_name: str = FieldInfo(alias="displayName")

    format: ItemDataUnionMember6Format

    render: ItemDataUnionMember6Render

    type: Literal["number"]


class ItemDataUnionMember7(BaseModel):
    display_name: str = FieldInfo(alias="displayName")

    type: Literal["string"]

    description: Optional[str] = None


class ItemDataUnionMember8(BaseModel):
    type: Literal["Assign"]

    description: Optional[str] = None

    title: Optional[str] = None


class ItemDataUnionMember9Format(BaseModel):
    time: Optional[bool] = None

    zone: Union[bool, str, None] = None


class ItemDataUnionMember9(BaseModel):
    type: Literal["DateTime"]

    description: Optional[str] = None

    format: Optional[ItemDataUnionMember9Format] = None

    title: Optional[str] = None


class ItemDataUnionMember10Format(BaseModel):
    time: Optional[bool] = None

    zone: Union[bool, str, None] = None


class ItemDataUnionMember10(BaseModel):
    type: Literal["DateRange"]

    description: Optional[str] = None

    format: Optional[ItemDataUnionMember10Format] = None

    title: Optional[str] = None


ItemData: TypeAlias = Union[
    ItemDataType,
    ItemDataType,
    ItemDataType,
    ItemDataUnionMember3,
    ItemDataUnionMember4,
    ItemDataUnionMember5,
    ItemDataUnionMember6,
    ItemDataUnionMember7,
    ItemDataUnionMember8,
    ItemDataUnionMember9,
    ItemDataUnionMember10,
    ItemDataType,
    ItemDataType,
    ItemDataType,
]


class Item(BaseModel):
    id: str

    data: ItemData


class ProjectListFieldsResponse(BaseModel):
    items: List[Item]

    ok: Literal[True]
