# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "PublicAgentUpdateResponse",
    "Item",
    "ItemData",
    "ItemDataAvatar",
    "ItemDataAvatarUnionMember0",
    "ItemDataAvatarUnionMember0Data",
    "ItemDataAvatarUnionMember0DataFile",
    "ItemDataAvatarUnionMember1",
    "ItemDataAvatarUnionMember1Data",
    "ItemDataConversationStarter",
    "ItemPreferences",
    "ItemPreferencesMeta",
]


class ItemDataAvatarUnionMember0DataFile(BaseModel):
    id: str

    extension: str

    mimetype: str

    namespace: str

    owner_id: str = FieldInfo(alias="ownerID")

    s3_key_original: str = FieldInfo(alias="s3KeyOriginal")

    size: float

    description: Optional[str] = None

    document_id: Optional[str] = FieldInfo(alias="documentID", default=None)

    metadata: Optional[Dict[str, object]] = None

    name: Optional[str] = None

    node_id: Optional[str] = FieldInfo(alias="nodeID", default=None)

    owner_type: Optional[str] = FieldInfo(alias="ownerType", default=None)

    space_id: Optional[str] = FieldInfo(alias="spaceID", default=None)

    type: Optional[str] = None

    user_id: Optional[float] = FieldInfo(alias="userID", default=None)

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ItemDataAvatarUnionMember0Data(BaseModel):
    file: ItemDataAvatarUnionMember0DataFile


class ItemDataAvatarUnionMember0(BaseModel):
    data: ItemDataAvatarUnionMember0Data

    type: Literal["custom"]


class ItemDataAvatarUnionMember1Data(BaseModel):
    value: str
    """Pick the most suitable emoji for this agent."""


class ItemDataAvatarUnionMember1(BaseModel):
    data: ItemDataAvatarUnionMember1Data

    type: Literal["emoji"]


ItemDataAvatar: TypeAlias = Union[ItemDataAvatarUnionMember0, ItemDataAvatarUnionMember1]


class ItemDataConversationStarter(BaseModel):
    id: str

    text: str


class ItemData(BaseModel):
    avatar: Optional[ItemDataAvatar] = None

    conversation_starters: Optional[List[ItemDataConversationStarter]] = FieldInfo(
        alias="conversationStarters", default=None
    )


class ItemPreferencesMeta(BaseModel):
    description: Optional[str] = None

    image: Optional[object] = None

    title: Optional[str] = None


class ItemPreferences(BaseModel):
    auto_end_chats: Optional[bool] = FieldInfo(alias="autoEndChats", default=None)

    can_copy_knowledge: Optional[bool] = FieldInfo(alias="canCopyKnowledge", default=None)

    hide_branding: Optional[bool] = FieldInfo(alias="hideBranding", default=None)

    meta: Optional[ItemPreferencesMeta] = None

    mode: Optional[Literal["template", "chatbot"]] = None

    theme: Optional[Literal["light", "dark", "auto"]] = None


class Item(BaseModel):
    id: str

    data: ItemData

    name: str

    preferences: ItemPreferences


class PublicAgentUpdateResponse(BaseModel):
    item: Item

    ok: Literal[True]
