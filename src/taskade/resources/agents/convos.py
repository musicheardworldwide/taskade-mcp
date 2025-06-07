# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.agents import convo_list_params
from ...types.agents.convo_list_response import ConvoListResponse
from ...types.agents.convo_retrieve_response import ConvoRetrieveResponse

__all__ = ["ConvosResource", "AsyncConvosResource"]


class ConvosResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConvosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#accessing-raw-response-data-eg-headers
        """
        return ConvosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConvosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#with_streaming_response
        """
        return ConvosResourceWithStreamingResponse(self)

    def retrieve(
        self,
        convo_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConvoRetrieveResponse:
        """
        Get agent conversation by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not convo_id:
            raise ValueError(f"Expected a non-empty value for `convo_id` but received {convo_id!r}")
        return self._get(
            f"/agents/{agent_id}/convos/{convo_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConvoRetrieveResponse,
        )

    def list(
        self,
        agent_id: str,
        *,
        limit: float | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConvoListResponse:
        """
        Get agent conversations

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/agents/{agent_id}/convos/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    convo_list_params.ConvoListParams,
                ),
            ),
            cast_to=ConvoListResponse,
        )


class AsyncConvosResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConvosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConvosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConvosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#with_streaming_response
        """
        return AsyncConvosResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        convo_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConvoRetrieveResponse:
        """
        Get agent conversation by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not convo_id:
            raise ValueError(f"Expected a non-empty value for `convo_id` but received {convo_id!r}")
        return await self._get(
            f"/agents/{agent_id}/convos/{convo_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConvoRetrieveResponse,
        )

    async def list(
        self,
        agent_id: str,
        *,
        limit: float | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConvoListResponse:
        """
        Get agent conversations

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/agents/{agent_id}/convos/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    convo_list_params.ConvoListParams,
                ),
            ),
            cast_to=ConvoListResponse,
        )


class ConvosResourceWithRawResponse:
    def __init__(self, convos: ConvosResource) -> None:
        self._convos = convos

        self.retrieve = to_raw_response_wrapper(
            convos.retrieve,
        )
        self.list = to_raw_response_wrapper(
            convos.list,
        )


class AsyncConvosResourceWithRawResponse:
    def __init__(self, convos: AsyncConvosResource) -> None:
        self._convos = convos

        self.retrieve = async_to_raw_response_wrapper(
            convos.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            convos.list,
        )


class ConvosResourceWithStreamingResponse:
    def __init__(self, convos: ConvosResource) -> None:
        self._convos = convos

        self.retrieve = to_streamed_response_wrapper(
            convos.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            convos.list,
        )


class AsyncConvosResourceWithStreamingResponse:
    def __init__(self, convos: AsyncConvosResource) -> None:
        self._convos = convos

        self.retrieve = async_to_streamed_response_wrapper(
            convos.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            convos.list,
        )
