# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from .date import (
    DateResource,
    AsyncDateResource,
    DateResourceWithRawResponse,
    AsyncDateResourceWithRawResponse,
    DateResourceWithStreamingResponse,
    AsyncDateResourceWithStreamingResponse,
)
from .note import (
    NoteResource,
    AsyncNoteResource,
    NoteResourceWithRawResponse,
    AsyncNoteResourceWithRawResponse,
    NoteResourceWithStreamingResponse,
    AsyncNoteResourceWithStreamingResponse,
)
from .fields import (
    FieldsResource,
    AsyncFieldsResource,
    FieldsResourceWithRawResponse,
    AsyncFieldsResourceWithRawResponse,
    FieldsResourceWithStreamingResponse,
    AsyncFieldsResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from .assignees import (
    AssigneesResource,
    AsyncAssigneesResource,
    AssigneesResourceWithRawResponse,
    AsyncAssigneesResourceWithRawResponse,
    AssigneesResourceWithStreamingResponse,
    AsyncAssigneesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.projects import task_list_params, task_move_params, task_create_params, task_update_params
from ....types.projects.task_list_response import TaskListResponse
from ....types.projects.task_move_response import TaskMoveResponse
from ....types.projects.task_create_response import TaskCreateResponse
from ....types.projects.task_delete_response import TaskDeleteResponse
from ....types.projects.task_update_response import TaskUpdateResponse
from ....types.projects.task_complete_response import TaskCompleteResponse
from ....types.projects.task_retrieve_response import TaskRetrieveResponse
from ....types.projects.task_uncomplete_response import TaskUncompleteResponse

__all__ = ["TasksResource", "AsyncTasksResource"]


class TasksResource(SyncAPIResource):
    @cached_property
    def assignees(self) -> AssigneesResource:
        return AssigneesResource(self._client)

    @cached_property
    def date(self) -> DateResource:
        return DateResource(self._client)

    @cached_property
    def note(self) -> NoteResource:
        return NoteResource(self._client)

    @cached_property
    def fields(self) -> FieldsResource:
        return FieldsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#accessing-raw-response-data-eg-headers
        """
        return TasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#with_streaming_response
        """
        return TasksResourceWithStreamingResponse(self)

    def create(
        self,
        project_id: str,
        *,
        tasks: Iterable[task_create_params.Task],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskCreateResponse:
        """
        Create one or more tasks in a project

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            f"/projects/{project_id}/tasks/",
            body=maybe_transform({"tasks": tasks}, task_create_params.TaskCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskCreateResponse,
        )

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
    ) -> TaskRetrieveResponse:
        """
        Get task with id

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
            f"/projects/{project_id}/tasks/{task_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskRetrieveResponse,
        )

    def update(
        self,
        task_id: str,
        *,
        project_id: str,
        content: str,
        content_type: Literal["text/markdown", "text/plain"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskUpdateResponse:
        """
        Update task.

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
            f"/projects/{project_id}/tasks/{task_id}",
            body=maybe_transform(
                {
                    "content": content,
                    "content_type": content_type,
                },
                task_update_params.TaskUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskUpdateResponse,
        )

    def list(
        self,
        project_id: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskListResponse:
        """
        Get all tasks for a project

        Args:
          after: Parameter for cursor-based pagination. Specify task ID to get tasks after it. Do
              not specify both before and after.

          before: Parameter for cursor-based pagination. Specify task ID to get tasks before it.
              Do not specify both before and after.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get(
            f"/projects/{project_id}/tasks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    task_list_params.TaskListParams,
                ),
            ),
            cast_to=TaskListResponse,
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
    ) -> TaskDeleteResponse:
        """
        Delete a task in a project

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
            f"/projects/{project_id}/tasks/{task_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskDeleteResponse,
        )

    def complete(
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
    ) -> TaskCompleteResponse:
        """
        Complete a task in a project

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
        return self._post(
            f"/projects/{project_id}/tasks/{task_id}/complete",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskCompleteResponse,
        )

    def move(
        self,
        task_id: str,
        *,
        project_id: str,
        target: task_move_params.Target,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskMoveResponse:
        """
        Move a task within the project

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
            f"/projects/{project_id}/tasks/{task_id}/move",
            body=maybe_transform({"target": target}, task_move_params.TaskMoveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskMoveResponse,
        )

    def uncomplete(
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
    ) -> TaskUncompleteResponse:
        """
        Mark a task as incomplete in a project

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
        return self._post(
            f"/projects/{project_id}/tasks/{task_id}/uncomplete",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskUncompleteResponse,
        )


class AsyncTasksResource(AsyncAPIResource):
    @cached_property
    def assignees(self) -> AsyncAssigneesResource:
        return AsyncAssigneesResource(self._client)

    @cached_property
    def date(self) -> AsyncDateResource:
        return AsyncDateResource(self._client)

    @cached_property
    def note(self) -> AsyncNoteResource:
        return AsyncNoteResource(self._client)

    @cached_property
    def fields(self) -> AsyncFieldsResource:
        return AsyncFieldsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#with_streaming_response
        """
        return AsyncTasksResourceWithStreamingResponse(self)

    async def create(
        self,
        project_id: str,
        *,
        tasks: Iterable[task_create_params.Task],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskCreateResponse:
        """
        Create one or more tasks in a project

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            f"/projects/{project_id}/tasks/",
            body=await async_maybe_transform({"tasks": tasks}, task_create_params.TaskCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskCreateResponse,
        )

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
    ) -> TaskRetrieveResponse:
        """
        Get task with id

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
            f"/projects/{project_id}/tasks/{task_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskRetrieveResponse,
        )

    async def update(
        self,
        task_id: str,
        *,
        project_id: str,
        content: str,
        content_type: Literal["text/markdown", "text/plain"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskUpdateResponse:
        """
        Update task.

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
            f"/projects/{project_id}/tasks/{task_id}",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "content_type": content_type,
                },
                task_update_params.TaskUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskUpdateResponse,
        )

    async def list(
        self,
        project_id: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskListResponse:
        """
        Get all tasks for a project

        Args:
          after: Parameter for cursor-based pagination. Specify task ID to get tasks after it. Do
              not specify both before and after.

          before: Parameter for cursor-based pagination. Specify task ID to get tasks before it.
              Do not specify both before and after.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._get(
            f"/projects/{project_id}/tasks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    task_list_params.TaskListParams,
                ),
            ),
            cast_to=TaskListResponse,
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
    ) -> TaskDeleteResponse:
        """
        Delete a task in a project

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
            f"/projects/{project_id}/tasks/{task_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskDeleteResponse,
        )

    async def complete(
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
    ) -> TaskCompleteResponse:
        """
        Complete a task in a project

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
        return await self._post(
            f"/projects/{project_id}/tasks/{task_id}/complete",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskCompleteResponse,
        )

    async def move(
        self,
        task_id: str,
        *,
        project_id: str,
        target: task_move_params.Target,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskMoveResponse:
        """
        Move a task within the project

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
            f"/projects/{project_id}/tasks/{task_id}/move",
            body=await async_maybe_transform({"target": target}, task_move_params.TaskMoveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskMoveResponse,
        )

    async def uncomplete(
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
    ) -> TaskUncompleteResponse:
        """
        Mark a task as incomplete in a project

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
        return await self._post(
            f"/projects/{project_id}/tasks/{task_id}/uncomplete",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskUncompleteResponse,
        )


class TasksResourceWithRawResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.create = to_raw_response_wrapper(
            tasks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            tasks.retrieve,
        )
        self.update = to_raw_response_wrapper(
            tasks.update,
        )
        self.list = to_raw_response_wrapper(
            tasks.list,
        )
        self.delete = to_raw_response_wrapper(
            tasks.delete,
        )
        self.complete = to_raw_response_wrapper(
            tasks.complete,
        )
        self.move = to_raw_response_wrapper(
            tasks.move,
        )
        self.uncomplete = to_raw_response_wrapper(
            tasks.uncomplete,
        )

    @cached_property
    def assignees(self) -> AssigneesResourceWithRawResponse:
        return AssigneesResourceWithRawResponse(self._tasks.assignees)

    @cached_property
    def date(self) -> DateResourceWithRawResponse:
        return DateResourceWithRawResponse(self._tasks.date)

    @cached_property
    def note(self) -> NoteResourceWithRawResponse:
        return NoteResourceWithRawResponse(self._tasks.note)

    @cached_property
    def fields(self) -> FieldsResourceWithRawResponse:
        return FieldsResourceWithRawResponse(self._tasks.fields)


class AsyncTasksResourceWithRawResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.create = async_to_raw_response_wrapper(
            tasks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            tasks.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            tasks.update,
        )
        self.list = async_to_raw_response_wrapper(
            tasks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tasks.delete,
        )
        self.complete = async_to_raw_response_wrapper(
            tasks.complete,
        )
        self.move = async_to_raw_response_wrapper(
            tasks.move,
        )
        self.uncomplete = async_to_raw_response_wrapper(
            tasks.uncomplete,
        )

    @cached_property
    def assignees(self) -> AsyncAssigneesResourceWithRawResponse:
        return AsyncAssigneesResourceWithRawResponse(self._tasks.assignees)

    @cached_property
    def date(self) -> AsyncDateResourceWithRawResponse:
        return AsyncDateResourceWithRawResponse(self._tasks.date)

    @cached_property
    def note(self) -> AsyncNoteResourceWithRawResponse:
        return AsyncNoteResourceWithRawResponse(self._tasks.note)

    @cached_property
    def fields(self) -> AsyncFieldsResourceWithRawResponse:
        return AsyncFieldsResourceWithRawResponse(self._tasks.fields)


class TasksResourceWithStreamingResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.create = to_streamed_response_wrapper(
            tasks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            tasks.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            tasks.update,
        )
        self.list = to_streamed_response_wrapper(
            tasks.list,
        )
        self.delete = to_streamed_response_wrapper(
            tasks.delete,
        )
        self.complete = to_streamed_response_wrapper(
            tasks.complete,
        )
        self.move = to_streamed_response_wrapper(
            tasks.move,
        )
        self.uncomplete = to_streamed_response_wrapper(
            tasks.uncomplete,
        )

    @cached_property
    def assignees(self) -> AssigneesResourceWithStreamingResponse:
        return AssigneesResourceWithStreamingResponse(self._tasks.assignees)

    @cached_property
    def date(self) -> DateResourceWithStreamingResponse:
        return DateResourceWithStreamingResponse(self._tasks.date)

    @cached_property
    def note(self) -> NoteResourceWithStreamingResponse:
        return NoteResourceWithStreamingResponse(self._tasks.note)

    @cached_property
    def fields(self) -> FieldsResourceWithStreamingResponse:
        return FieldsResourceWithStreamingResponse(self._tasks.fields)


class AsyncTasksResourceWithStreamingResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.create = async_to_streamed_response_wrapper(
            tasks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            tasks.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            tasks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            tasks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tasks.delete,
        )
        self.complete = async_to_streamed_response_wrapper(
            tasks.complete,
        )
        self.move = async_to_streamed_response_wrapper(
            tasks.move,
        )
        self.uncomplete = async_to_streamed_response_wrapper(
            tasks.uncomplete,
        )

    @cached_property
    def assignees(self) -> AsyncAssigneesResourceWithStreamingResponse:
        return AsyncAssigneesResourceWithStreamingResponse(self._tasks.assignees)

    @cached_property
    def date(self) -> AsyncDateResourceWithStreamingResponse:
        return AsyncDateResourceWithStreamingResponse(self._tasks.date)

    @cached_property
    def note(self) -> AsyncNoteResourceWithStreamingResponse:
        return AsyncNoteResourceWithStreamingResponse(self._tasks.note)

    @cached_property
    def fields(self) -> AsyncFieldsResourceWithStreamingResponse:
        return AsyncFieldsResourceWithStreamingResponse(self._tasks.fields)
