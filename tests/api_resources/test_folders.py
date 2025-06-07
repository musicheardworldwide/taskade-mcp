# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from taskade import Taskade, AsyncTaskade
from tests.utils import assert_matches_type
from taskade.types import (
    FolderListMediasResponse,
    FolderListProjectsResponse,
    FolderGenerateAgentResponse,
    FolderListProjectTemplatesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFolders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_generate_agent(self, client: Taskade) -> None:
        folder = client.folders.generate_agent(
            folder_id="folderId",
            text="text",
        )
        assert_matches_type(FolderGenerateAgentResponse, folder, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_generate_agent(self, client: Taskade) -> None:
        response = client.folders.with_raw_response.generate_agent(
            folder_id="folderId",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FolderGenerateAgentResponse, folder, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_generate_agent(self, client: Taskade) -> None:
        with client.folders.with_streaming_response.generate_agent(
            folder_id="folderId",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FolderGenerateAgentResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_generate_agent(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.folders.with_raw_response.generate_agent(
                folder_id="",
                text="text",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list_medias(self, client: Taskade) -> None:
        folder = client.folders.list_medias(
            folder_id="folderId",
        )
        assert_matches_type(FolderListMediasResponse, folder, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_medias_with_all_params(self, client: Taskade) -> None:
        folder = client.folders.list_medias(
            folder_id="folderId",
            limit=0,
            page=0,
        )
        assert_matches_type(FolderListMediasResponse, folder, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_medias(self, client: Taskade) -> None:
        response = client.folders.with_raw_response.list_medias(
            folder_id="folderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FolderListMediasResponse, folder, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_medias(self, client: Taskade) -> None:
        with client.folders.with_streaming_response.list_medias(
            folder_id="folderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FolderListMediasResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_medias(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.folders.with_raw_response.list_medias(
                folder_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list_project_templates(self, client: Taskade) -> None:
        folder = client.folders.list_project_templates(
            folder_id="folderId",
        )
        assert_matches_type(FolderListProjectTemplatesResponse, folder, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_project_templates_with_all_params(self, client: Taskade) -> None:
        folder = client.folders.list_project_templates(
            folder_id="folderId",
            limit=0,
            page=0,
        )
        assert_matches_type(FolderListProjectTemplatesResponse, folder, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_project_templates(self, client: Taskade) -> None:
        response = client.folders.with_raw_response.list_project_templates(
            folder_id="folderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FolderListProjectTemplatesResponse, folder, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_project_templates(self, client: Taskade) -> None:
        with client.folders.with_streaming_response.list_project_templates(
            folder_id="folderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FolderListProjectTemplatesResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_project_templates(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.folders.with_raw_response.list_project_templates(
                folder_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list_projects(self, client: Taskade) -> None:
        folder = client.folders.list_projects(
            "folderId",
        )
        assert_matches_type(FolderListProjectsResponse, folder, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_projects(self, client: Taskade) -> None:
        response = client.folders.with_raw_response.list_projects(
            "folderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FolderListProjectsResponse, folder, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_projects(self, client: Taskade) -> None:
        with client.folders.with_streaming_response.list_projects(
            "folderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FolderListProjectsResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_projects(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.folders.with_raw_response.list_projects(
                "",
            )


class TestAsyncFolders:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_generate_agent(self, async_client: AsyncTaskade) -> None:
        folder = await async_client.folders.generate_agent(
            folder_id="folderId",
            text="text",
        )
        assert_matches_type(FolderGenerateAgentResponse, folder, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_generate_agent(self, async_client: AsyncTaskade) -> None:
        response = await async_client.folders.with_raw_response.generate_agent(
            folder_id="folderId",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FolderGenerateAgentResponse, folder, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_generate_agent(self, async_client: AsyncTaskade) -> None:
        async with async_client.folders.with_streaming_response.generate_agent(
            folder_id="folderId",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FolderGenerateAgentResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_generate_agent(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.folders.with_raw_response.generate_agent(
                folder_id="",
                text="text",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_medias(self, async_client: AsyncTaskade) -> None:
        folder = await async_client.folders.list_medias(
            folder_id="folderId",
        )
        assert_matches_type(FolderListMediasResponse, folder, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_medias_with_all_params(self, async_client: AsyncTaskade) -> None:
        folder = await async_client.folders.list_medias(
            folder_id="folderId",
            limit=0,
            page=0,
        )
        assert_matches_type(FolderListMediasResponse, folder, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_medias(self, async_client: AsyncTaskade) -> None:
        response = await async_client.folders.with_raw_response.list_medias(
            folder_id="folderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FolderListMediasResponse, folder, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_medias(self, async_client: AsyncTaskade) -> None:
        async with async_client.folders.with_streaming_response.list_medias(
            folder_id="folderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FolderListMediasResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_medias(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.folders.with_raw_response.list_medias(
                folder_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_project_templates(self, async_client: AsyncTaskade) -> None:
        folder = await async_client.folders.list_project_templates(
            folder_id="folderId",
        )
        assert_matches_type(FolderListProjectTemplatesResponse, folder, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_project_templates_with_all_params(self, async_client: AsyncTaskade) -> None:
        folder = await async_client.folders.list_project_templates(
            folder_id="folderId",
            limit=0,
            page=0,
        )
        assert_matches_type(FolderListProjectTemplatesResponse, folder, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_project_templates(self, async_client: AsyncTaskade) -> None:
        response = await async_client.folders.with_raw_response.list_project_templates(
            folder_id="folderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FolderListProjectTemplatesResponse, folder, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_project_templates(self, async_client: AsyncTaskade) -> None:
        async with async_client.folders.with_streaming_response.list_project_templates(
            folder_id="folderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FolderListProjectTemplatesResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_project_templates(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.folders.with_raw_response.list_project_templates(
                folder_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_projects(self, async_client: AsyncTaskade) -> None:
        folder = await async_client.folders.list_projects(
            "folderId",
        )
        assert_matches_type(FolderListProjectsResponse, folder, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_projects(self, async_client: AsyncTaskade) -> None:
        response = await async_client.folders.with_raw_response.list_projects(
            "folderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FolderListProjectsResponse, folder, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_projects(self, async_client: AsyncTaskade) -> None:
        async with async_client.folders.with_streaming_response.list_projects(
            "folderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FolderListProjectsResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_projects(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.folders.with_raw_response.list_projects(
                "",
            )
