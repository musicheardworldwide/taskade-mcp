# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Project"]


class Project(BaseModel):
    id: str
    """Unique identifier for the project.

    An alphanumeric string that is 16 characters long.
    """

    name: Optional[str] = None
    """The project’s name or title."""
