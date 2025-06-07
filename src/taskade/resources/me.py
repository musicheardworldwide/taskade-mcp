# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import me_list_projects_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.me_list_projects_response import MeListProjectsResponse

__all__ = ["MeResource", "AsyncMeResource"]


class MeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#accessing-raw-response-data-eg-headers
        """
        return MeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#with_streaming_response
        """
        return MeResourceWithStreamingResponse(self)

    def list_projects(
        self,
        *,
        limit: float | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        sort: Literal["viewed-asc", "viewed-desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MeListProjectsResponse:
        """
        Get all projects of mine

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/me/projects",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                        "sort": sort,
                    },
                    me_list_projects_params.MeListProjectsParams,
                ),
            ),
            cast_to=MeListProjectsResponse,
        )


class AsyncMeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#with_streaming_response
        """
        return AsyncMeResourceWithStreamingResponse(self)

    async def list_projects(
        self,
        *,
        limit: float | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        sort: Literal["viewed-asc", "viewed-desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MeListProjectsResponse:
        """
        Get all projects of mine

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/me/projects",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                        "sort": sort,
                    },
                    me_list_projects_params.MeListProjectsParams,
                ),
            ),
            cast_to=MeListProjectsResponse,
        )


class MeResourceWithRawResponse:
    def __init__(self, me: MeResource) -> None:
        self._me = me

        self.list_projects = to_raw_response_wrapper(
            me.list_projects,
        )


class AsyncMeResourceWithRawResponse:
    def __init__(self, me: AsyncMeResource) -> None:
        self._me = me

        self.list_projects = async_to_raw_response_wrapper(
            me.list_projects,
        )


class MeResourceWithStreamingResponse:
    def __init__(self, me: MeResource) -> None:
        self._me = me

        self.list_projects = to_streamed_response_wrapper(
            me.list_projects,
        )


class AsyncMeResourceWithStreamingResponse:
    def __init__(self, me: AsyncMeResource) -> None:
        self._me = me

        self.list_projects = async_to_streamed_response_wrapper(
            me.list_projects,
        )
