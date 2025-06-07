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
from ..types.media_delete_response import MediaDeleteResponse
from ..types.media_retrieve_response import MediaRetrieveResponse

__all__ = ["MediasResource", "AsyncMediasResource"]


class MediasResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MediasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#accessing-raw-response-data-eg-headers
        """
        return MediasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MediasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#with_streaming_response
        """
        return MediasResourceWithStreamingResponse(self)

    def retrieve(
        self,
        media_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MediaRetrieveResponse:
        """
        Get media with id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not media_id:
            raise ValueError(f"Expected a non-empty value for `media_id` but received {media_id!r}")
        return self._get(
            f"/medias/{media_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaRetrieveResponse,
        )

    def delete(
        self,
        media_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MediaDeleteResponse:
        """
        Delete a media

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not media_id:
            raise ValueError(f"Expected a non-empty value for `media_id` but received {media_id!r}")
        return self._delete(
            f"/medias/{media_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaDeleteResponse,
        )


class AsyncMediasResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMediasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMediasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMediasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#with_streaming_response
        """
        return AsyncMediasResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        media_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MediaRetrieveResponse:
        """
        Get media with id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not media_id:
            raise ValueError(f"Expected a non-empty value for `media_id` but received {media_id!r}")
        return await self._get(
            f"/medias/{media_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaRetrieveResponse,
        )

    async def delete(
        self,
        media_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MediaDeleteResponse:
        """
        Delete a media

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not media_id:
            raise ValueError(f"Expected a non-empty value for `media_id` but received {media_id!r}")
        return await self._delete(
            f"/medias/{media_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaDeleteResponse,
        )


class MediasResourceWithRawResponse:
    def __init__(self, medias: MediasResource) -> None:
        self._medias = medias

        self.retrieve = to_raw_response_wrapper(
            medias.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            medias.delete,
        )


class AsyncMediasResourceWithRawResponse:
    def __init__(self, medias: AsyncMediasResource) -> None:
        self._medias = medias

        self.retrieve = async_to_raw_response_wrapper(
            medias.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            medias.delete,
        )


class MediasResourceWithStreamingResponse:
    def __init__(self, medias: MediasResource) -> None:
        self._medias = medias

        self.retrieve = to_streamed_response_wrapper(
            medias.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            medias.delete,
        )


class AsyncMediasResourceWithStreamingResponse:
    def __init__(self, medias: AsyncMediasResource) -> None:
        self._medias = medias

        self.retrieve = async_to_streamed_response_wrapper(
            medias.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            medias.delete,
        )
