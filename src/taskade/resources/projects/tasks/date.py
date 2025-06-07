# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.projects.tasks import date_update_params
from ....types.projects.tasks.task_date_param import TaskDateParam
from ....types.projects.tasks.date_delete_response import DateDeleteResponse
from ....types.projects.tasks.date_update_response import DateUpdateResponse
from ....types.projects.tasks.date_retrieve_response import DateRetrieveResponse

__all__ = ["DateResource", "AsyncDateResource"]


class DateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#accessing-raw-response-data-eg-headers
        """
        return DateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#with_streaming_response
        """
        return DateResourceWithStreamingResponse(self)

    def retrieve(
        self,
        task_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DateRetrieveResponse:
        """
        Get the date of a task

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._get(
            f"/projects/{project_id}/tasks/{task_id}/date",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DateRetrieveResponse,
        )

    def update(
        self,
        task_id: str,
        *,
        project_id: str,
        start: TaskDateParam,
        end: TaskDateParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DateUpdateResponse:
        """
        Create or update date for a task

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._put(
            f"/projects/{project_id}/tasks/{task_id}/date",
            body=maybe_transform(
                {
                    "start": start,
                    "end": end,
                },
                date_update_params.DateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DateUpdateResponse,
        )

    def delete(
        self,
        task_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DateDeleteResponse:
        """
        Delete date of a task

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._delete(
            f"/projects/{project_id}/tasks/{task_id}/date",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DateDeleteResponse,
        )


class AsyncDateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#with_streaming_response
        """
        return AsyncDateResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        task_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DateRetrieveResponse:
        """
        Get the date of a task

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._get(
            f"/projects/{project_id}/tasks/{task_id}/date",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DateRetrieveResponse,
        )

    async def update(
        self,
        task_id: str,
        *,
        project_id: str,
        start: TaskDateParam,
        end: TaskDateParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DateUpdateResponse:
        """
        Create or update date for a task

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._put(
            f"/projects/{project_id}/tasks/{task_id}/date",
            body=await async_maybe_transform(
                {
                    "start": start,
                    "end": end,
                },
                date_update_params.DateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DateUpdateResponse,
        )

    async def delete(
        self,
        task_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DateDeleteResponse:
        """
        Delete date of a task

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._delete(
            f"/projects/{project_id}/tasks/{task_id}/date",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DateDeleteResponse,
        )


class DateResourceWithRawResponse:
    def __init__(self, date: DateResource) -> None:
        self._date = date

        self.retrieve = to_raw_response_wrapper(
            date.retrieve,
        )
        self.update = to_raw_response_wrapper(
            date.update,
        )
        self.delete = to_raw_response_wrapper(
            date.delete,
        )


class AsyncDateResourceWithRawResponse:
    def __init__(self, date: AsyncDateResource) -> None:
        self._date = date

        self.retrieve = async_to_raw_response_wrapper(
            date.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            date.update,
        )
        self.delete = async_to_raw_response_wrapper(
            date.delete,
        )


class DateResourceWithStreamingResponse:
    def __init__(self, date: DateResource) -> None:
        self._date = date

        self.retrieve = to_streamed_response_wrapper(
            date.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            date.update,
        )
        self.delete = to_streamed_response_wrapper(
            date.delete,
        )


class AsyncDateResourceWithStreamingResponse:
    def __init__(self, date: AsyncDateResource) -> None:
        self._date = date

        self.retrieve = async_to_streamed_response_wrapper(
            date.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            date.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            date.delete,
        )
