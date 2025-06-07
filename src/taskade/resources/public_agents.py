# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.public_agent_retrieve_response import PublicAgentRetrieveResponse

__all__ = ["PublicAgentsResource", "AsyncPublicAgentsResource"]


class PublicAgentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PublicAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#accessing-raw-response-data-eg-headers
        """
        return PublicAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PublicAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#with_streaming_response
        """
        return PublicAgentsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        public_agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PublicAgentRetrieveResponse:
        """
        Get public agent by public agent ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not public_agent_id:
            raise ValueError(f"Expected a non-empty value for `public_agent_id` but received {public_agent_id!r}")
        return self._get(
            f"/public-agents/{public_agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicAgentRetrieveResponse,
        )


class AsyncPublicAgentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPublicAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPublicAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPublicAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#with_streaming_response
        """
        return AsyncPublicAgentsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        public_agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PublicAgentRetrieveResponse:
        """
        Get public agent by public agent ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not public_agent_id:
            raise ValueError(f"Expected a non-empty value for `public_agent_id` but received {public_agent_id!r}")
        return await self._get(
            f"/public-agents/{public_agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicAgentRetrieveResponse,
        )


class PublicAgentsResourceWithRawResponse:
    def __init__(self, public_agents: PublicAgentsResource) -> None:
        self._public_agents = public_agents

        self.retrieve = to_raw_response_wrapper(
            public_agents.retrieve,
        )


class AsyncPublicAgentsResourceWithRawResponse:
    def __init__(self, public_agents: AsyncPublicAgentsResource) -> None:
        self._public_agents = public_agents

        self.retrieve = async_to_raw_response_wrapper(
            public_agents.retrieve,
        )


class PublicAgentsResourceWithStreamingResponse:
    def __init__(self, public_agents: PublicAgentsResource) -> None:
        self._public_agents = public_agents

        self.retrieve = to_streamed_response_wrapper(
            public_agents.retrieve,
        )


class AsyncPublicAgentsResourceWithStreamingResponse:
    def __init__(self, public_agents: AsyncPublicAgentsResource) -> None:
        self._public_agents = public_agents

        self.retrieve = async_to_streamed_response_wrapper(
            public_agents.retrieve,
        )
