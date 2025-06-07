# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.projects.share_link_enable_response import ShareLinkEnableResponse
from ...types.projects.share_link_retrieve_response import ShareLinkRetrieveResponse

__all__ = ["ShareLinkResource", "AsyncShareLinkResource"]


class ShareLinkResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ShareLinkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/musicheardworldwide/taskade-mcp#accessing-raw-response-data-eg-headers
        """
        return ShareLinkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ShareLinkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/musicheardworldwide/taskade-mcp#with_streaming_response
        """
        return ShareLinkResourceWithStreamingResponse(self)

    def retrieve(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ShareLinkRetrieveResponse:
        """
        Get share link for the project

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get(
            f"/projects/{project_id}/shareLink",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShareLinkRetrieveResponse,
        )

    def enable(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ShareLinkEnableResponse:
        """
        Enable share link in the project

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._put(
            f"/projects/{project_id}/shareLink",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShareLinkEnableResponse,
        )


class AsyncShareLinkResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncShareLinkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/musicheardworldwide/taskade-mcp#accessing-raw-response-data-eg-headers
        """
        return AsyncShareLinkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncShareLinkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/musicheardworldwide/taskade-mcp#with_streaming_response
        """
        return AsyncShareLinkResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ShareLinkRetrieveResponse:
        """
        Get share link for the project

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._get(
            f"/projects/{project_id}/shareLink",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShareLinkRetrieveResponse,
        )

    async def enable(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ShareLinkEnableResponse:
        """
        Enable share link in the project

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._put(
            f"/projects/{project_id}/shareLink",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShareLinkEnableResponse,
        )


class ShareLinkResourceWithRawResponse:
    def __init__(self, share_link: ShareLinkResource) -> None:
        self._share_link = share_link

        self.retrieve = to_raw_response_wrapper(
            share_link.retrieve,
        )
        self.enable = to_raw_response_wrapper(
            share_link.enable,
        )


class AsyncShareLinkResourceWithRawResponse:
    def __init__(self, share_link: AsyncShareLinkResource) -> None:
        self._share_link = share_link

        self.retrieve = async_to_raw_response_wrapper(
            share_link.retrieve,
        )
        self.enable = async_to_raw_response_wrapper(
            share_link.enable,
        )


class ShareLinkResourceWithStreamingResponse:
    def __init__(self, share_link: ShareLinkResource) -> None:
        self._share_link = share_link

        self.retrieve = to_streamed_response_wrapper(
            share_link.retrieve,
        )
        self.enable = to_streamed_response_wrapper(
            share_link.enable,
        )


class AsyncShareLinkResourceWithStreamingResponse:
    def __init__(self, share_link: AsyncShareLinkResource) -> None:
        self._share_link = share_link

        self.retrieve = async_to_streamed_response_wrapper(
            share_link.retrieve,
        )
        self.enable = async_to_streamed_response_wrapper(
            share_link.enable,
        )
