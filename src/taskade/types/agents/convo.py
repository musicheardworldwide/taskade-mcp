# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Convo", "Data", "DataLlm", "DataLlmUnionMember0", "DataLlmUnionMember1"]


class DataLlmUnionMember0(BaseModel):
    name: Literal[
        "gpt-3.5-turbo",
        "gpt-4o",
        "gpt-4-turbo",
        "gpt-4o-mini",
        "o3-mini:low",
        "o3-mini:medium",
        "o3-mini:high",
        "gpt-4.1",
        "gpt-4.1-mini",
        "gpt-4.1-nano",
        "o4-mini:low",
        "o4-mini:medium",
        "o4-mini:high",
    ]

    type: Literal["openai"]


class DataLlmUnionMember1(BaseModel):
    name: Literal[
        "anthropic/claude-3.5-sonnet",
        "anthropic/claude-3.5-haiku",
        "anthropic/claude-3.7-sonnet",
        "anthropic/claude-4.0-sonnet",
        "anthropic/claude-4.0-opus",
    ]

    type: Literal["anthropic"]


DataLlm: TypeAlias = Union[DataLlmUnionMember0, DataLlmUnionMember1]


class Data(BaseModel):
    ended_at: Optional[float] = FieldInfo(alias="endedAt", default=None)

    llm: Optional[DataLlm] = None


class Convo(BaseModel):
    id: str

    data: Data

    space_agent_id: str

    status: Literal["in_progress", "idle", "requires_review"]

    title: Optional[str] = None
