# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import workspace_create_project_params
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
from ..types.workspace_list_response import WorkspaceListResponse
from ..types.workspace_list_folders_response import WorkspaceListFoldersResponse
from ..types.workspace_create_project_response import WorkspaceCreateProjectResponse

__all__ = ["WorkspacesResource", "AsyncWorkspacesResource"]


class WorkspacesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WorkspacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#accessing-raw-response-data-eg-headers
        """
        return WorkspacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkspacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#with_streaming_response
        """
        return WorkspacesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkspaceListResponse:
        """Get all workspaces for a user"""
        return self._get(
            "/workspaces",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceListResponse,
        )

    def create_project(
        self,
        workspace_id: str,
        *,
        content: str,
        content_type: Literal["text/markdown"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkspaceCreateProjectResponse:
        """
        Create a project in a workspace

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._post(
            f"/workspaces/{workspace_id}/projects",
            body=maybe_transform(
                {
                    "content": content,
                    "content_type": content_type,
                },
                workspace_create_project_params.WorkspaceCreateProjectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceCreateProjectResponse,
        )

    def list_folders(
        self,
        workspace_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkspaceListFoldersResponse:
        """
        Get all folders for a workspace

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get(
            f"/workspaces/{workspace_id}/folders",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceListFoldersResponse,
        )


class AsyncWorkspacesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWorkspacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkspacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkspacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/taskade-python#with_streaming_response
        """
        return AsyncWorkspacesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkspaceListResponse:
        """Get all workspaces for a user"""
        return await self._get(
            "/workspaces",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceListResponse,
        )

    async def create_project(
        self,
        workspace_id: str,
        *,
        content: str,
        content_type: Literal["text/markdown"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkspaceCreateProjectResponse:
        """
        Create a project in a workspace

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._post(
            f"/workspaces/{workspace_id}/projects",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "content_type": content_type,
                },
                workspace_create_project_params.WorkspaceCreateProjectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceCreateProjectResponse,
        )

    async def list_folders(
        self,
        workspace_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkspaceListFoldersResponse:
        """
        Get all folders for a workspace

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._get(
            f"/workspaces/{workspace_id}/folders",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceListFoldersResponse,
        )


class WorkspacesResourceWithRawResponse:
    def __init__(self, workspaces: WorkspacesResource) -> None:
        self._workspaces = workspaces

        self.list = to_raw_response_wrapper(
            workspaces.list,
        )
        self.create_project = to_raw_response_wrapper(
            workspaces.create_project,
        )
        self.list_folders = to_raw_response_wrapper(
            workspaces.list_folders,
        )


class AsyncWorkspacesResourceWithRawResponse:
    def __init__(self, workspaces: AsyncWorkspacesResource) -> None:
        self._workspaces = workspaces

        self.list = async_to_raw_response_wrapper(
            workspaces.list,
        )
        self.create_project = async_to_raw_response_wrapper(
            workspaces.create_project,
        )
        self.list_folders = async_to_raw_response_wrapper(
            workspaces.list_folders,
        )


class WorkspacesResourceWithStreamingResponse:
    def __init__(self, workspaces: WorkspacesResource) -> None:
        self._workspaces = workspaces

        self.list = to_streamed_response_wrapper(
            workspaces.list,
        )
        self.create_project = to_streamed_response_wrapper(
            workspaces.create_project,
        )
        self.list_folders = to_streamed_response_wrapper(
            workspaces.list_folders,
        )


class AsyncWorkspacesResourceWithStreamingResponse:
    def __init__(self, workspaces: AsyncWorkspacesResource) -> None:
        self._workspaces = workspaces

        self.list = async_to_streamed_response_wrapper(
            workspaces.list,
        )
        self.create_project = async_to_streamed_response_wrapper(
            workspaces.create_project,
        )
        self.list_folders = async_to_streamed_response_wrapper(
            workspaces.list_folders,
        )
