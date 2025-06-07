# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from taskade import Taskade, AsyncTaskade
from tests.utils import assert_matches_type
from taskade.types.projects.tasks import (
    AssigneeListResponse,
    AssigneeRemoveResponse,
    AssigneeUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssignees:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Taskade) -> None:
        assignee = client.projects.tasks.assignees.update(
            task_id="taskId",
            project_id="projectId",
            handles=["x"],
        )
        assert_matches_type(AssigneeUpdateResponse, assignee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Taskade) -> None:
        response = client.projects.tasks.assignees.with_raw_response.update(
            task_id="taskId",
            project_id="projectId",
            handles=["x"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assignee = response.parse()
        assert_matches_type(AssigneeUpdateResponse, assignee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Taskade) -> None:
        with client.projects.tasks.assignees.with_streaming_response.update(
            task_id="taskId",
            project_id="projectId",
            handles=["x"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assignee = response.parse()
            assert_matches_type(AssigneeUpdateResponse, assignee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.tasks.assignees.with_raw_response.update(
                task_id="taskId",
                project_id="",
                handles=["x"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.projects.tasks.assignees.with_raw_response.update(
                task_id="",
                project_id="projectId",
                handles=["x"],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Taskade) -> None:
        assignee = client.projects.tasks.assignees.list(
            task_id="taskId",
            project_id="projectId",
        )
        assert_matches_type(AssigneeListResponse, assignee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Taskade) -> None:
        response = client.projects.tasks.assignees.with_raw_response.list(
            task_id="taskId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assignee = response.parse()
        assert_matches_type(AssigneeListResponse, assignee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Taskade) -> None:
        with client.projects.tasks.assignees.with_streaming_response.list(
            task_id="taskId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assignee = response.parse()
            assert_matches_type(AssigneeListResponse, assignee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.tasks.assignees.with_raw_response.list(
                task_id="taskId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.projects.tasks.assignees.with_raw_response.list(
                task_id="",
                project_id="projectId",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_remove(self, client: Taskade) -> None:
        assignee = client.projects.tasks.assignees.remove(
            assignee_handle="assigneeHandle",
            project_id="projectId",
            task_id="taskId",
        )
        assert_matches_type(AssigneeRemoveResponse, assignee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_remove(self, client: Taskade) -> None:
        response = client.projects.tasks.assignees.with_raw_response.remove(
            assignee_handle="assigneeHandle",
            project_id="projectId",
            task_id="taskId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assignee = response.parse()
        assert_matches_type(AssigneeRemoveResponse, assignee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_remove(self, client: Taskade) -> None:
        with client.projects.tasks.assignees.with_streaming_response.remove(
            assignee_handle="assigneeHandle",
            project_id="projectId",
            task_id="taskId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assignee = response.parse()
            assert_matches_type(AssigneeRemoveResponse, assignee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_remove(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.tasks.assignees.with_raw_response.remove(
                assignee_handle="assigneeHandle",
                project_id="",
                task_id="taskId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.projects.tasks.assignees.with_raw_response.remove(
                assignee_handle="assigneeHandle",
                project_id="projectId",
                task_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assignee_handle` but received ''"):
            client.projects.tasks.assignees.with_raw_response.remove(
                assignee_handle="",
                project_id="projectId",
                task_id="taskId",
            )


class TestAsyncAssignees:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncTaskade) -> None:
        assignee = await async_client.projects.tasks.assignees.update(
            task_id="taskId",
            project_id="projectId",
            handles=["x"],
        )
        assert_matches_type(AssigneeUpdateResponse, assignee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTaskade) -> None:
        response = await async_client.projects.tasks.assignees.with_raw_response.update(
            task_id="taskId",
            project_id="projectId",
            handles=["x"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assignee = await response.parse()
        assert_matches_type(AssigneeUpdateResponse, assignee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTaskade) -> None:
        async with async_client.projects.tasks.assignees.with_streaming_response.update(
            task_id="taskId",
            project_id="projectId",
            handles=["x"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assignee = await response.parse()
            assert_matches_type(AssigneeUpdateResponse, assignee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.tasks.assignees.with_raw_response.update(
                task_id="taskId",
                project_id="",
                handles=["x"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.projects.tasks.assignees.with_raw_response.update(
                task_id="",
                project_id="projectId",
                handles=["x"],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncTaskade) -> None:
        assignee = await async_client.projects.tasks.assignees.list(
            task_id="taskId",
            project_id="projectId",
        )
        assert_matches_type(AssigneeListResponse, assignee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTaskade) -> None:
        response = await async_client.projects.tasks.assignees.with_raw_response.list(
            task_id="taskId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assignee = await response.parse()
        assert_matches_type(AssigneeListResponse, assignee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTaskade) -> None:
        async with async_client.projects.tasks.assignees.with_streaming_response.list(
            task_id="taskId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assignee = await response.parse()
            assert_matches_type(AssigneeListResponse, assignee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.tasks.assignees.with_raw_response.list(
                task_id="taskId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.projects.tasks.assignees.with_raw_response.list(
                task_id="",
                project_id="projectId",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_remove(self, async_client: AsyncTaskade) -> None:
        assignee = await async_client.projects.tasks.assignees.remove(
            assignee_handle="assigneeHandle",
            project_id="projectId",
            task_id="taskId",
        )
        assert_matches_type(AssigneeRemoveResponse, assignee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncTaskade) -> None:
        response = await async_client.projects.tasks.assignees.with_raw_response.remove(
            assignee_handle="assigneeHandle",
            project_id="projectId",
            task_id="taskId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assignee = await response.parse()
        assert_matches_type(AssigneeRemoveResponse, assignee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncTaskade) -> None:
        async with async_client.projects.tasks.assignees.with_streaming_response.remove(
            assignee_handle="assigneeHandle",
            project_id="projectId",
            task_id="taskId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assignee = await response.parse()
            assert_matches_type(AssigneeRemoveResponse, assignee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.tasks.assignees.with_raw_response.remove(
                assignee_handle="assigneeHandle",
                project_id="",
                task_id="taskId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.projects.tasks.assignees.with_raw_response.remove(
                assignee_handle="assigneeHandle",
                project_id="projectId",
                task_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assignee_handle` but received ''"):
            await async_client.projects.tasks.assignees.with_raw_response.remove(
                assignee_handle="",
                project_id="projectId",
                task_id="taskId",
            )
