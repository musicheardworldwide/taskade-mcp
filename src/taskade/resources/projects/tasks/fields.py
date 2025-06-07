# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union

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
from ....types.projects.tasks import field_update_params
from ....types.projects.tasks.field_list_response import FieldListResponse
from ....types.projects.tasks.field_delete_response import FieldDeleteResponse
from ....types.projects.tasks.field_update_response import FieldUpdateResponse
from ....types.projects.tasks.field_retrieve_response import FieldRetrieveResponse

__all__ = ["FieldsResource", "AsyncFieldsResource"]


class FieldsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FieldsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#accessing-raw-response-data-eg-headers
        """
        return FieldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FieldsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#with_streaming_response
        """
        return FieldsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        field_id: str,
        *,
        project_id: str,
        task_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FieldRetrieveResponse:
        """
        Get the field value of a task

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
        if not field_id:
            raise ValueError(f"Expected a non-empty value for `field_id` but received {field_id!r}")
        return self._get(
            f"/projects/{project_id}/tasks/{task_id}/fields/{field_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FieldRetrieveResponse,
        )

    def update(
        self,
        field_id: str,
        *,
        project_id: str,
        task_id: str,
        value: Union[float, str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FieldUpdateResponse:
        """
        Update/create the field value of a task

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
        if not field_id:
            raise ValueError(f"Expected a non-empty value for `field_id` but received {field_id!r}")
        return self._put(
            f"/projects/{project_id}/tasks/{task_id}/fields/{field_id}",
            body=maybe_transform({"value": value}, field_update_params.FieldUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FieldUpdateResponse,
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
    ) -> FieldListResponse:
        """
        Get all field values for a task

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
            f"/projects/{project_id}/tasks/{task_id}/fields",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FieldListResponse,
        )

    def delete(
        self,
        field_id: str,
        *,
        project_id: str,
        task_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FieldDeleteResponse:
        """
        Delete the field value of a task

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
        if not field_id:
            raise ValueError(f"Expected a non-empty value for `field_id` but received {field_id!r}")
        return self._delete(
            f"/projects/{project_id}/tasks/{task_id}/fields/{field_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FieldDeleteResponse,
        )


class AsyncFieldsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFieldsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFieldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFieldsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#with_streaming_response
        """
        return AsyncFieldsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        field_id: str,
        *,
        project_id: str,
        task_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FieldRetrieveResponse:
        """
        Get the field value of a task

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
        if not field_id:
            raise ValueError(f"Expected a non-empty value for `field_id` but received {field_id!r}")
        return await self._get(
            f"/projects/{project_id}/tasks/{task_id}/fields/{field_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FieldRetrieveResponse,
        )

    async def update(
        self,
        field_id: str,
        *,
        project_id: str,
        task_id: str,
        value: Union[float, str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FieldUpdateResponse:
        """
        Update/create the field value of a task

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
        if not field_id:
            raise ValueError(f"Expected a non-empty value for `field_id` but received {field_id!r}")
        return await self._put(
            f"/projects/{project_id}/tasks/{task_id}/fields/{field_id}",
            body=await async_maybe_transform({"value": value}, field_update_params.FieldUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FieldUpdateResponse,
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
    ) -> FieldListResponse:
        """
        Get all field values for a task

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
            f"/projects/{project_id}/tasks/{task_id}/fields",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FieldListResponse,
        )

    async def delete(
        self,
        field_id: str,
        *,
        project_id: str,
        task_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FieldDeleteResponse:
        """
        Delete the field value of a task

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
        if not field_id:
            raise ValueError(f"Expected a non-empty value for `field_id` but received {field_id!r}")
        return await self._delete(
            f"/projects/{project_id}/tasks/{task_id}/fields/{field_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FieldDeleteResponse,
        )


class FieldsResourceWithRawResponse:
    def __init__(self, fields: FieldsResource) -> None:
        self._fields = fields

        self.retrieve = to_raw_response_wrapper(
            fields.retrieve,
        )
        self.update = to_raw_response_wrapper(
            fields.update,
        )
        self.list = to_raw_response_wrapper(
            fields.list,
        )
        self.delete = to_raw_response_wrapper(
            fields.delete,
        )


class AsyncFieldsResourceWithRawResponse:
    def __init__(self, fields: AsyncFieldsResource) -> None:
        self._fields = fields

        self.retrieve = async_to_raw_response_wrapper(
            fields.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            fields.update,
        )
        self.list = async_to_raw_response_wrapper(
            fields.list,
        )
        self.delete = async_to_raw_response_wrapper(
            fields.delete,
        )


class FieldsResourceWithStreamingResponse:
    def __init__(self, fields: FieldsResource) -> None:
        self._fields = fields

        self.retrieve = to_streamed_response_wrapper(
            fields.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            fields.update,
        )
        self.list = to_streamed_response_wrapper(
            fields.list,
        )
        self.delete = to_streamed_response_wrapper(
            fields.delete,
        )


class AsyncFieldsResourceWithStreamingResponse:
    def __init__(self, fields: AsyncFieldsResource) -> None:
        self._fields = fields

        self.retrieve = async_to_streamed_response_wrapper(
            fields.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            fields.update,
        )
        self.list = async_to_streamed_response_wrapper(
            fields.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            fields.delete,
        )
