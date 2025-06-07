# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

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
from ....types.projects.tasks import assignee_update_params
from ....types.projects.tasks.assignee_list_response import AssigneeListResponse
from ....types.projects.tasks.assignee_remove_response import AssigneeRemoveResponse
from ....types.projects.tasks.assignee_update_response import AssigneeUpdateResponse

__all__ = ["AssigneesResource", "AsyncAssigneesResource"]


class AssigneesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AssigneesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#accessing-raw-response-data-eg-headers
        """
        return AssigneesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssigneesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#with_streaming_response
        """
        return AssigneesResourceWithStreamingResponse(self)

    def update(
        self,
        task_id: str,
        *,
        project_id: str,
        handles: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssigneeUpdateResponse:
        """
        Task assignment

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
            f"/projects/{project_id}/tasks/{task_id}/assignees",
            body=maybe_transform({"handles": handles}, assignee_update_params.AssigneeUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssigneeUpdateResponse,
        )

    def list(
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
    ) -> AssigneeListResponse:
        """
        Get the assignees of a task

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
            f"/projects/{project_id}/tasks/{task_id}/assignees",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssigneeListResponse,
        )

    def remove(
        self,
        assignee_handle: str,
        *,
        project_id: str,
        task_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssigneeRemoveResponse:
        """
        Remove assignee from a task

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
        if not assignee_handle:
            raise ValueError(f"Expected a non-empty value for `assignee_handle` but received {assignee_handle!r}")
        return self._delete(
            f"/projects/{project_id}/tasks/{task_id}/assignees/{assignee_handle}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssigneeRemoveResponse,
        )


class AsyncAssigneesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAssigneesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssigneesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssigneesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#with_streaming_response
        """
        return AsyncAssigneesResourceWithStreamingResponse(self)

    async def update(
        self,
        task_id: str,
        *,
        project_id: str,
        handles: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssigneeUpdateResponse:
        """
        Task assignment

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
            f"/projects/{project_id}/tasks/{task_id}/assignees",
            body=await async_maybe_transform({"handles": handles}, assignee_update_params.AssigneeUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssigneeUpdateResponse,
        )

    async def list(
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
    ) -> AssigneeListResponse:
        """
        Get the assignees of a task

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
            f"/projects/{project_id}/tasks/{task_id}/assignees",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssigneeListResponse,
        )

    async def remove(
        self,
        assignee_handle: str,
        *,
        project_id: str,
        task_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssigneeRemoveResponse:
        """
        Remove assignee from a task

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
        if not assignee_handle:
            raise ValueError(f"Expected a non-empty value for `assignee_handle` but received {assignee_handle!r}")
        return await self._delete(
            f"/projects/{project_id}/tasks/{task_id}/assignees/{assignee_handle}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssigneeRemoveResponse,
        )


class AssigneesResourceWithRawResponse:
    def __init__(self, assignees: AssigneesResource) -> None:
        self._assignees = assignees

        self.update = to_raw_response_wrapper(
            assignees.update,
        )
        self.list = to_raw_response_wrapper(
            assignees.list,
        )
        self.remove = to_raw_response_wrapper(
            assignees.remove,
        )


class AsyncAssigneesResourceWithRawResponse:
    def __init__(self, assignees: AsyncAssigneesResource) -> None:
        self._assignees = assignees

        self.update = async_to_raw_response_wrapper(
            assignees.update,
        )
        self.list = async_to_raw_response_wrapper(
            assignees.list,
        )
        self.remove = async_to_raw_response_wrapper(
            assignees.remove,
        )


class AssigneesResourceWithStreamingResponse:
    def __init__(self, assignees: AssigneesResource) -> None:
        self._assignees = assignees

        self.update = to_streamed_response_wrapper(
            assignees.update,
        )
        self.list = to_streamed_response_wrapper(
            assignees.list,
        )
        self.remove = to_streamed_response_wrapper(
            assignees.remove,
        )


class AsyncAssigneesResourceWithStreamingResponse:
    def __init__(self, assignees: AsyncAssigneesResource) -> None:
        self._assignees = assignees

        self.update = async_to_streamed_response_wrapper(
            assignees.update,
        )
        self.list = async_to_streamed_response_wrapper(
            assignees.list,
        )
        self.remove = async_to_streamed_response_wrapper(
            assignees.remove,
        )
