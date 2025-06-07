# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentUpdateParams", "Data", "DataCommand", "DataAvatar", "DataAvatarData"]


class AgentUpdateParams(TypedDict, total=False):
    data: Data

    name: str


class DataCommand(TypedDict, total=False):
    id: Required[str]
    """ID based on the name in snake case."""

    name: Required[str]
    """Human-readable name of the command in title case.

    This should probably be a verb.
    """

    prompt: Required[str]
    """Tell the agent what this command will do.

    It should be positioned as a direct instruction to the agent. At least 30 words.
    """

    mode: Literal["default", "plan-and-execute-v1", "plan-and-execute-v2"]


class DataAvatarData(TypedDict, total=False):
    value: Required[str]
    """Pick the most suitable emoji for this agent."""


class DataAvatar(TypedDict, total=False):
    data: Required[DataAvatarData]

    type: Required[Literal["emoji"]]


class Data(TypedDict, total=False):
    commands: Required[Iterable[DataCommand]]

    avatar: DataAvatar

    description: str
    """Role and purpose of agent, positioned as a direct instruction to the agent.

    Example: "You are a doctor that helps save lives.". At least 100 words.
    """

    input_placeholder: Annotated[str, PropertyInfo(alias="inputPlaceholder")]

    knowledge_enabled: Annotated[bool, PropertyInfo(alias="knowledgeEnabled")]

    language: str
    """The language of the agent, e.g. en-US, zh-Hans"""

    tone: Literal[
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
