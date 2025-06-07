# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AgentEnablePublicAccessResponse"]


class AgentEnablePublicAccessResponse(BaseModel):
    ok: Literal[True]

    public_url: str = FieldInfo(alias="publicUrl")
