# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SpaceAgent", "Data", "DataCommand", "DataAvatar", "DataAvatarData"]


class DataCommand(BaseModel):
    id: str
    """ID based on the name in snake case."""

    name: str
    """Human-readable name of the command in title case.

    This should probably be a verb.
    """

    prompt: str
    """Tell the agent what this command will do.

    It should be positioned as a direct instruction to the agent. At least 30 words.
    """

    mode: Optional[Literal["default", "plan-and-execute-v1", "plan-and-execute-v2"]] = None


class DataAvatarData(BaseModel):
    value: str
    """Pick the most suitable emoji for this agent."""


class DataAvatar(BaseModel):
    data: DataAvatarData

    type: Literal["emoji"]


class Data(BaseModel):
    commands: List[DataCommand]

    avatar: Optional[DataAvatar] = None

    description: Optional[str] = None
    """Role and purpose of agent, positioned as a direct instruction to the agent.

    Example: "You are a doctor that helps save lives.". At least 100 words.
    """

    input_placeholder: Optional[str] = FieldInfo(alias="inputPlaceholder", default=None)

    knowledge_enabled: Optional[bool] = FieldInfo(alias="knowledgeEnabled", default=None)

    language: Optional[str] = None
    """The language of the agent, e.g. en-US, zh-Hans"""

    tone: Optional[
        Literal[
            "authoritative",
            "clinical",
            "cold",
            "confident",
            "cynical",
            "emotional",
            "empathetic",
            "formal",
            "friendly",
            "humourous",
            "informal",
            "ironic",
            "optimistic",
            "pessimistic",
            "playful",
            "sarcastic",
            "serious",
            "sympathetic",
            "tentative",
            "warm",
            "creative",
            "inspiring",
            "casual",
        ]
    ] = None


class SpaceAgent(BaseModel):
    id: str

    data: Data

    name: str

    space_id: str
