# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from taskade import Taskade, AsyncTaskade
from tests.utils import assert_matches_type
from taskade.types import (
    ProjectCopyResponse,
    ProjectCreateResponse,
    ProjectRestoreResponse,
    ProjectCompleteResponse,
    ProjectRetrieveResponse,
    ProjectListBlocksResponse,
    ProjectListFieldsResponse,
    ProjectListMembersResponse,
    ProjectCreateFromTemplateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProjects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Taskade) -> None:
        project = client.projects.create(
            content="content",
            content_type="text/markdown",
            folder_id="x",
        )
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Taskade) -> None:
        response = client.projects.with_raw_response.create(
            content="content",
            content_type="text/markdown",
            folder_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Taskade) -> None:
        with client.projects.with_streaming_response.create(
            content="content",
            content_type="text/markdown",
            folder_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectCreateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Taskade) -> None:
        project = client.projects.retrieve(
            "projectId",
        )
        assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Taskade) -> None:
        response = client.projects.with_raw_response.retrieve(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Taskade) -> None:
        with client.projects.with_streaming_response.retrieve(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_complete(self, client: Taskade) -> None:
        project = client.projects.complete(
            "projectId",
        )
        assert_matches_type(ProjectCompleteResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_complete(self, client: Taskade) -> None:
        response = client.projects.with_raw_response.complete(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectCompleteResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_complete(self, client: Taskade) -> None:
        with client.projects.with_streaming_response.complete(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectCompleteResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_complete(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.with_raw_response.complete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_copy(self, client: Taskade) -> None:
        project = client.projects.copy(
            project_id="projectId",
            folder_id="x",
        )
        assert_matches_type(ProjectCopyResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_copy_with_all_params(self, client: Taskade) -> None:
        project = client.projects.copy(
            project_id="projectId",
            folder_id="x",
            project_title="x",
        )
        assert_matches_type(ProjectCopyResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_copy(self, client: Taskade) -> None:
        response = client.projects.with_raw_response.copy(
            project_id="projectId",
            folder_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectCopyResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_copy(self, client: Taskade) -> None:
        with client.projects.with_streaming_response.copy(
            project_id="projectId",
            folder_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectCopyResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_copy(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.with_raw_response.copy(
                project_id="",
                folder_id="x",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_from_template(self, client: Taskade) -> None:
        project = client.projects.create_from_template(
            folder_id="x",
            template_id="x",
        )
        assert_matches_type(ProjectCreateFromTemplateResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_from_template(self, client: Taskade) -> None:
        response = client.projects.with_raw_response.create_from_template(
            folder_id="x",
            template_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectCreateFromTemplateResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_from_template(self, client: Taskade) -> None:
        with client.projects.with_streaming_response.create_from_template(
            folder_id="x",
            template_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectCreateFromTemplateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_blocks(self, client: Taskade) -> None:
        project = client.projects.list_blocks(
            project_id="projectId",
        )
        assert_matches_type(ProjectListBlocksResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_blocks_with_all_params(self, client: Taskade) -> None:
        project = client.projects.list_blocks(
            project_id="projectId",
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
        )
        assert_matches_type(ProjectListBlocksResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_blocks(self, client: Taskade) -> None:
        response = client.projects.with_raw_response.list_blocks(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectListBlocksResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_blocks(self, client: Taskade) -> None:
        with client.projects.with_streaming_response.list_blocks(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectListBlocksResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_blocks(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.with_raw_response.list_blocks(
                project_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list_fields(self, client: Taskade) -> None:
        project = client.projects.list_fields(
            "projectId",
        )
        assert_matches_type(ProjectListFieldsResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_fields(self, client: Taskade) -> None:
        response = client.projects.with_raw_response.list_fields(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectListFieldsResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_fields(self, client: Taskade) -> None:
        with client.projects.with_streaming_response.list_fields(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectListFieldsResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_fields(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.with_raw_response.list_fields(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list_members(self, client: Taskade) -> None:
        project = client.projects.list_members(
            project_id="projectId",
        )
        assert_matches_type(ProjectListMembersResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_members_with_all_params(self, client: Taskade) -> None:
        project = client.projects.list_members(
            project_id="projectId",
            limit=0,
            page=0,
        )
        assert_matches_type(ProjectListMembersResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_members(self, client: Taskade) -> None:
        response = client.projects.with_raw_response.list_members(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectListMembersResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_members(self, client: Taskade) -> None:
        with client.projects.with_streaming_response.list_members(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectListMembersResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_members(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.with_raw_response.list_members(
                project_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_restore(self, client: Taskade) -> None:
        project = client.projects.restore(
            "projectId",
        )
        assert_matches_type(ProjectRestoreResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_restore(self, client: Taskade) -> None:
        response = client.projects.with_raw_response.restore(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectRestoreResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_restore(self, client: Taskade) -> None:
        with client.projects.with_streaming_response.restore(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectRestoreResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_restore(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.with_raw_response.restore(
                "",
            )


class TestAsyncProjects:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncTaskade) -> None:
        project = await async_client.projects.create(
            content="content",
            content_type="text/markdown",
            folder_id="x",
        )
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTaskade) -> None:
        response = await async_client.projects.with_raw_response.create(
            content="content",
            content_type="text/markdown",
            folder_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTaskade) -> None:
        async with async_client.projects.with_streaming_response.create(
            content="content",
            content_type="text/markdown",
            folder_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectCreateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTaskade) -> None:
        project = await async_client.projects.retrieve(
            "projectId",
        )
        assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTaskade) -> None:
        response = await async_client.projects.with_raw_response.retrieve(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTaskade) -> None:
        async with async_client.projects.with_streaming_response.retrieve(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_complete(self, async_client: AsyncTaskade) -> None:
        project = await async_client.projects.complete(
            "projectId",
        )
        assert_matches_type(ProjectCompleteResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_complete(self, async_client: AsyncTaskade) -> None:
        response = await async_client.projects.with_raw_response.complete(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectCompleteResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_complete(self, async_client: AsyncTaskade) -> None:
        async with async_client.projects.with_streaming_response.complete(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectCompleteResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_complete(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.with_raw_response.complete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_copy(self, async_client: AsyncTaskade) -> None:
        project = await async_client.projects.copy(
            project_id="projectId",
            folder_id="x",
        )
        assert_matches_type(ProjectCopyResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_copy_with_all_params(self, async_client: AsyncTaskade) -> None:
        project = await async_client.projects.copy(
            project_id="projectId",
            folder_id="x",
            project_title="x",
        )
        assert_matches_type(ProjectCopyResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_copy(self, async_client: AsyncTaskade) -> None:
        response = await async_client.projects.with_raw_response.copy(
            project_id="projectId",
            folder_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectCopyResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_copy(self, async_client: AsyncTaskade) -> None:
        async with async_client.projects.with_streaming_response.copy(
            project_id="projectId",
            folder_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectCopyResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_copy(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.with_raw_response.copy(
                project_id="",
                folder_id="x",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_from_template(self, async_client: AsyncTaskade) -> None:
        project = await async_client.projects.create_from_template(
            folder_id="x",
            template_id="x",
        )
        assert_matches_type(ProjectCreateFromTemplateResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_from_template(self, async_client: AsyncTaskade) -> None:
        response = await async_client.projects.with_raw_response.create_from_template(
            folder_id="x",
            template_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectCreateFromTemplateResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_from_template(self, async_client: AsyncTaskade) -> None:
        async with async_client.projects.with_streaming_response.create_from_template(
            folder_id="x",
            template_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectCreateFromTemplateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_blocks(self, async_client: AsyncTaskade) -> None:
        project = await async_client.projects.list_blocks(
            project_id="projectId",
        )
        assert_matches_type(ProjectListBlocksResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_blocks_with_all_params(self, async_client: AsyncTaskade) -> None:
        project = await async_client.projects.list_blocks(
            project_id="projectId",
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
        )
        assert_matches_type(ProjectListBlocksResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_blocks(self, async_client: AsyncTaskade) -> None:
        response = await async_client.projects.with_raw_response.list_blocks(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectListBlocksResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_blocks(self, async_client: AsyncTaskade) -> None:
        async with async_client.projects.with_streaming_response.list_blocks(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectListBlocksResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_blocks(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.with_raw_response.list_blocks(
                project_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_fields(self, async_client: AsyncTaskade) -> None:
        project = await async_client.projects.list_fields(
            "projectId",
        )
        assert_matches_type(ProjectListFieldsResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_fields(self, async_client: AsyncTaskade) -> None:
        response = await async_client.projects.with_raw_response.list_fields(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectListFieldsResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_fields(self, async_client: AsyncTaskade) -> None:
        async with async_client.projects.with_streaming_response.list_fields(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectListFieldsResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_fields(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.with_raw_response.list_fields(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_members(self, async_client: AsyncTaskade) -> None:
        project = await async_client.projects.list_members(
            project_id="projectId",
        )
        assert_matches_type(ProjectListMembersResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_members_with_all_params(self, async_client: AsyncTaskade) -> None:
        project = await async_client.projects.list_members(
            project_id="projectId",
            limit=0,
            page=0,
        )
        assert_matches_type(ProjectListMembersResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_members(self, async_client: AsyncTaskade) -> None:
        response = await async_client.projects.with_raw_response.list_members(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectListMembersResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_members(self, async_client: AsyncTaskade) -> None:
        async with async_client.projects.with_streaming_response.list_members(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectListMembersResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_members(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.with_raw_response.list_members(
                project_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_restore(self, async_client: AsyncTaskade) -> None:
        project = await async_client.projects.restore(
            "projectId",
        )
        assert_matches_type(ProjectRestoreResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_restore(self, async_client: AsyncTaskade) -> None:
        response = await async_client.projects.with_raw_response.restore(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectRestoreResponse, project, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_restore(self, async_client: AsyncTaskade) -> None:
        async with async_client.projects.with_streaming_response.restore(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectRestoreResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_restore(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.with_raw_response.restore(
                "",
            )
