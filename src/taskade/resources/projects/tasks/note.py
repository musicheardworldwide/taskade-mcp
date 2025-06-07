# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from ....types.projects.tasks import note_update_params
from ....types.projects.tasks.note_delete_response import NoteDeleteResponse
from ....types.projects.tasks.note_update_response import NoteUpdateResponse
from ....types.projects.tasks.note_retrieve_response import NoteRetrieveResponse

__all__ = ["NoteResource", "AsyncNoteResource"]


class NoteResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NoteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#accessing-raw-response-data-eg-headers
        """
        return NoteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NoteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#with_streaming_response
        """
        return NoteResourceWithStreamingResponse(self)

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
    ) -> NoteRetrieveResponse:
        """
        Get the note of a task

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
            f"/projects/{project_id}/tasks/{task_id}/note",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoteRetrieveResponse,
        )

    def update(
        self,
        task_id: str,
        *,
        project_id: str,
        type: Literal["text/plain", "text/markdown"],
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NoteUpdateResponse:
        """
        Add/update a note to the task

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
            f"/projects/{project_id}/tasks/{task_id}/note",
            body=maybe_transform(
                {
                    "type": type,
                    "value": value,
                },
                note_update_params.NoteUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoteUpdateResponse,
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
    ) -> NoteDeleteResponse:
        """
        Delete the note of a task

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
            f"/projects/{project_id}/tasks/{task_id}/note",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoteDeleteResponse,
        )


class AsyncNoteResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNoteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNoteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNoteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#with_streaming_response
        """
        return AsyncNoteResourceWithStreamingResponse(self)

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
    ) -> NoteRetrieveResponse:
        """
        Get the note of a task

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
            f"/projects/{project_id}/tasks/{task_id}/note",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoteRetrieveResponse,
        )

    async def update(
        self,
        task_id: str,
        *,
        project_id: str,
        type: Literal["text/plain", "text/markdown"],
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NoteUpdateResponse:
        """
        Add/update a note to the task

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
            f"/projects/{project_id}/tasks/{task_id}/note",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "value": value,
                },
                note_update_params.NoteUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoteUpdateResponse,
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
    ) -> NoteDeleteResponse:
        """
        Delete the note of a task

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
            f"/projects/{project_id}/tasks/{task_id}/note",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoteDeleteResponse,
        )


class NoteResourceWithRawResponse:
    def __init__(self, note: NoteResource) -> None:
        self._note = note

        self.retrieve = to_raw_response_wrapper(
            note.retrieve,
        )
        self.update = to_raw_response_wrapper(
            note.update,
        )
        self.delete = to_raw_response_wrapper(
            note.delete,
        )


class AsyncNoteResourceWithRawResponse:
    def __init__(self, note: AsyncNoteResource) -> None:
        self._note = note

        self.retrieve = async_to_raw_response_wrapper(
            note.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            note.update,
        )
        self.delete = async_to_raw_response_wrapper(
            note.delete,
        )


class NoteResourceWithStreamingResponse:
    def __init__(self, note: NoteResource) -> None:
        self._note = note

        self.retrieve = to_streamed_response_wrapper(
            note.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            note.update,
        )
        self.delete = to_streamed_response_wrapper(
            note.delete,
        )


class AsyncNoteResourceWithStreamingResponse:
    def __init__(self, note: AsyncNoteResource) -> None:
        self._note = note

        self.retrieve = async_to_streamed_response_wrapper(
            note.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            note.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            note.delete,
        )
