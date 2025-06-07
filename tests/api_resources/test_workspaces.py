# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from taskade import Taskade, AsyncTaskade
from tests.utils import assert_matches_type
from taskade.types import (
    WorkspaceListResponse,
    WorkspaceListFoldersResponse,
    WorkspaceCreateProjectResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkspaces:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Taskade) -> None:
        workspace = client.workspaces.list()
        assert_matches_type(WorkspaceListResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Taskade) -> None:
        response = client.workspaces.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(WorkspaceListResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Taskade) -> None:
        with client.workspaces.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(WorkspaceListResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_create_project(self, client: Taskade) -> None:
        workspace = client.workspaces.create_project(
            workspace_id="workspaceId",
            content="content",
            content_type="text/markdown",
        )
        assert_matches_type(WorkspaceCreateProjectResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_project(self, client: Taskade) -> None:
        response = client.workspaces.with_raw_response.create_project(
            workspace_id="workspaceId",
            content="content",
            content_type="text/markdown",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(WorkspaceCreateProjectResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_project(self, client: Taskade) -> None:
        with client.workspaces.with_streaming_response.create_project(
            workspace_id="workspaceId",
            content="content",
            content_type="text/markdown",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(WorkspaceCreateProjectResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_project(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.with_raw_response.create_project(
                workspace_id="",
                content="content",
                content_type="text/markdown",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list_folders(self, client: Taskade) -> None:
        workspace = client.workspaces.list_folders(
            "workspaceId",
        )
        assert_matches_type(WorkspaceListFoldersResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_folders(self, client: Taskade) -> None:
        response = client.workspaces.with_raw_response.list_folders(
            "workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(WorkspaceListFoldersResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_folders(self, client: Taskade) -> None:
        with client.workspaces.with_streaming_response.list_folders(
            "workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(WorkspaceListFoldersResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_folders(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.with_raw_response.list_folders(
                "",
            )


class TestAsyncWorkspaces:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncTaskade) -> None:
        workspace = await async_client.workspaces.list()
        assert_matches_type(WorkspaceListResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTaskade) -> None:
        response = await async_client.workspaces.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(WorkspaceListResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTaskade) -> None:
        async with async_client.workspaces.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(WorkspaceListResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_project(self, async_client: AsyncTaskade) -> None:
        workspace = await async_client.workspaces.create_project(
            workspace_id="workspaceId",
            content="content",
            content_type="text/markdown",
        )
        assert_matches_type(WorkspaceCreateProjectResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_project(self, async_client: AsyncTaskade) -> None:
        response = await async_client.workspaces.with_raw_response.create_project(
            workspace_id="workspaceId",
            content="content",
            content_type="text/markdown",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(WorkspaceCreateProjectResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_project(self, async_client: AsyncTaskade) -> None:
        async with async_client.workspaces.with_streaming_response.create_project(
            workspace_id="workspaceId",
            content="content",
            content_type="text/markdown",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(WorkspaceCreateProjectResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_project(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.with_raw_response.create_project(
                workspace_id="",
                content="content",
                content_type="text/markdown",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_folders(self, async_client: AsyncTaskade) -> None:
        workspace = await async_client.workspaces.list_folders(
            "workspaceId",
        )
        assert_matches_type(WorkspaceListFoldersResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_folders(self, async_client: AsyncTaskade) -> None:
        response = await async_client.workspaces.with_raw_response.list_folders(
            "workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(WorkspaceListFoldersResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_folders(self, async_client: AsyncTaskade) -> None:
        async with async_client.workspaces.with_streaming_response.list_folders(
            "workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(WorkspaceListFoldersResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_folders(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.with_raw_response.list_folders(
                "",
            )
