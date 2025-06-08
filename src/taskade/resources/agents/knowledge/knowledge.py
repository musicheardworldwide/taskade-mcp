# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .media import (
    MediaResource,
    AsyncMediaResource,
    MediaResourceWithRawResponse,
    AsyncMediaResourceWithRawResponse,
    MediaResourceWithStreamingResponse,
    AsyncMediaResourceWithStreamingResponse,
)
from .project import (
    ProjectResource,
    AsyncProjectResource,
    ProjectResourceWithRawResponse,
    AsyncProjectResourceWithRawResponse,
    ProjectResourceWithStreamingResponse,
    AsyncProjectResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["KnowledgeResource", "AsyncKnowledgeResource"]


class KnowledgeResource(SyncAPIResource):
    @cached_property
    def project(self) -> ProjectResource:
        return ProjectResource(self._client)

    @cached_property
    def media(self) -> MediaResource:
        return MediaResource(self._client)

    @cached_property
    def with_raw_response(self) -> KnowledgeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/musicheardworldwide/taskade-mcp#accessing-raw-response-data-eg-headers
        """
        return KnowledgeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KnowledgeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/musicheardworldwide/taskade-mcp#with_streaming_response
        """
        return KnowledgeResourceWithStreamingResponse(self)


class AsyncKnowledgeResource(AsyncAPIResource):
    @cached_property
    def project(self) -> AsyncProjectResource:
        return AsyncProjectResource(self._client)

    @cached_property
    def media(self) -> AsyncMediaResource:
        return AsyncMediaResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncKnowledgeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/musicheardworldwide/taskade-mcp#accessing-raw-response-data-eg-headers
        """
        return AsyncKnowledgeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKnowledgeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/musicheardworldwide/taskade-mcp#with_streaming_response
        """
        return AsyncKnowledgeResourceWithStreamingResponse(self)


class KnowledgeResourceWithRawResponse:
    def __init__(self, knowledge: KnowledgeResource) -> None:
        self._knowledge = knowledge

    @cached_property
    def project(self) -> ProjectResourceWithRawResponse:
        return ProjectResourceWithRawResponse(self._knowledge.project)

    @cached_property
    def media(self) -> MediaResourceWithRawResponse:
        return MediaResourceWithRawResponse(self._knowledge.media)


class AsyncKnowledgeResourceWithRawResponse:
    def __init__(self, knowledge: AsyncKnowledgeResource) -> None:
        self._knowledge = knowledge

    @cached_property
    def project(self) -> AsyncProjectResourceWithRawResponse:
        return AsyncProjectResourceWithRawResponse(self._knowledge.project)

    @cached_property
    def media(self) -> AsyncMediaResourceWithRawResponse:
        return AsyncMediaResourceWithRawResponse(self._knowledge.media)


class KnowledgeResourceWithStreamingResponse:
    def __init__(self, knowledge: KnowledgeResource) -> None:
        self._knowledge = knowledge

    @cached_property
    def project(self) -> ProjectResourceWithStreamingResponse:
        return ProjectResourceWithStreamingResponse(self._knowledge.project)

    @cached_property
    def media(self) -> MediaResourceWithStreamingResponse:
        return MediaResourceWithStreamingResponse(self._knowledge.media)


class AsyncKnowledgeResourceWithStreamingResponse:
    def __init__(self, knowledge: AsyncKnowledgeResource) -> None:
        self._knowledge = knowledge

    @cached_property
    def project(self) -> AsyncProjectResourceWithStreamingResponse:
        return AsyncProjectResourceWithStreamingResponse(self._knowledge.project)

    @cached_property
    def media(self) -> AsyncMediaResourceWithStreamingResponse:
        return AsyncMediaResourceWithStreamingResponse(self._knowledge.media)
