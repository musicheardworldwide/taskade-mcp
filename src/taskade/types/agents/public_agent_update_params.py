# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicAgentUpdateParams", "Preferences", "PreferencesMeta", "PreferencesMetaImage"]


class PublicAgentUpdateParams(TypedDict, total=False):
    preferences: Required[Preferences]


class PreferencesMetaImageTyped(TypedDict, total=False):
    id: Required[str]

    extension: Required[str]

    mimetype: Required[str]

    namespace: Required[str]

    owner_id: Required[Annotated[str, PropertyInfo(alias="ownerID")]]

    s3_key_original: Required[Annotated[str, PropertyInfo(alias="s3KeyOriginal")]]

    size: Required[float]

    description: str

    document_id: Annotated[Optional[str], PropertyInfo(alias="documentID")]

    metadata: Dict[str, object]

    name: str

    node_id: Annotated[Optional[str], PropertyInfo(alias="nodeID")]

    owner_type: Annotated[Optional[str], PropertyInfo(alias="ownerType")]

    space_id: Annotated[Optional[str], PropertyInfo(alias="spaceID")]

    type: str

    user_id: Annotated[Optional[float], PropertyInfo(alias="userID")]


PreferencesMetaImage: TypeAlias = Union[PreferencesMetaImageTyped, Dict[str, object]]


class PreferencesMeta(TypedDict, total=False):
    description: str

    image: Optional[PreferencesMetaImage]

    title: str


class Preferences(TypedDict, total=False):
    auto_end_chats: Annotated[bool, PropertyInfo(alias="autoEndChats")]

    can_copy_knowledge: Annotated[bool, PropertyInfo(alias="canCopyKnowledge")]

    hide_branding: Annotated[bool, PropertyInfo(alias="hideBranding")]

    meta: PreferencesMeta

    mode: Literal["template", "chatbot"]

    theme: Literal["light", "dark", "auto"]
