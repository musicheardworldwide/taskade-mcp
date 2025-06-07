# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from taskade import Taskade, AsyncTaskade
from tests.utils import assert_matches_type
from taskade.types.projects import (
    TaskListResponse,
    TaskMoveResponse,
    TaskCreateResponse,
    TaskDeleteResponse,
    TaskUpdateResponse,
    TaskCompleteResponse,
    TaskRetrieveResponse,
    TaskUncompleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTasks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Taskade) -> None:
        task = client.projects.tasks.create(
            project_id="projectId",
            tasks=[{"placement": "afterbegin"}],
        )
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Taskade) -> None:
        response = client.projects.tasks.with_raw_response.create(
            project_id="projectId",
            tasks=[{"placement": "afterbegin"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Taskade) -> None:
        with client.projects.tasks.with_streaming_response.create(
            project_id="projectId",
            tasks=[{"placement": "afterbegin"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskCreateResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.tasks.with_raw_response.create(
                project_id="",
                tasks=[{"placement": "afterbegin"}],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Taskade) -> None:
        task = client.projects.tasks.retrieve(
            task_id="taskId",
            project_id="projectId",
        )
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Taskade) -> None:
        response = client.projects.tasks.with_raw_response.retrieve(
            task_id="taskId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Taskade) -> None:
        with client.projects.tasks.with_streaming_response.retrieve(
            task_id="taskId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskRetrieveResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.tasks.with_raw_response.retrieve(
                task_id="taskId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.projects.tasks.with_raw_response.retrieve(
                task_id="",
                project_id="projectId",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Taskade) -> None:
        task = client.projects.tasks.update(
            task_id="taskId",
            project_id="projectId",
            content="content",
            content_type="text/markdown",
        )
        assert_matches_type(TaskUpdateResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Taskade) -> None:
        response = client.projects.tasks.with_raw_response.update(
            task_id="taskId",
            project_id="projectId",
            content="content",
            content_type="text/markdown",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskUpdateResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Taskade) -> None:
        with client.projects.tasks.with_streaming_response.update(
            task_id="taskId",
            project_id="projectId",
            content="content",
            content_type="text/markdown",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskUpdateResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.tasks.with_raw_response.update(
                task_id="taskId",
                project_id="",
                content="content",
                content_type="text/markdown",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.projects.tasks.with_raw_response.update(
                task_id="",
                project_id="projectId",
                content="content",
                content_type="text/markdown",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Taskade) -> None:
        task = client.projects.tasks.list(
            project_id="projectId",
        )
        assert_matches_type(TaskListResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Taskade) -> None:
        task = client.projects.tasks.list(
            project_id="projectId",
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
        )
        assert_matches_type(TaskListResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Taskade) -> None:
        response = client.projects.tasks.with_raw_response.list(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskListResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Taskade) -> None:
        with client.projects.tasks.with_streaming_response.list(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskListResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.tasks.with_raw_response.list(
                project_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Taskade) -> None:
        task = client.projects.tasks.delete(
            task_id="taskId",
            project_id="projectId",
        )
        assert_matches_type(TaskDeleteResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Taskade) -> None:
        response = client.projects.tasks.with_raw_response.delete(
            task_id="taskId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskDeleteResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Taskade) -> None:
        with client.projects.tasks.with_streaming_response.delete(
            task_id="taskId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskDeleteResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.tasks.with_raw_response.delete(
                task_id="taskId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.projects.tasks.with_raw_response.delete(
                task_id="",
                project_id="projectId",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_complete(self, client: Taskade) -> None:
        task = client.projects.tasks.complete(
            task_id="taskId",
            project_id="projectId",
        )
        assert_matches_type(TaskCompleteResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_complete(self, client: Taskade) -> None:
        response = client.projects.tasks.with_raw_response.complete(
            task_id="taskId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskCompleteResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_complete(self, client: Taskade) -> None:
        with client.projects.tasks.with_streaming_response.complete(
            task_id="taskId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskCompleteResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_complete(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.tasks.with_raw_response.complete(
                task_id="taskId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.projects.tasks.with_raw_response.complete(
                task_id="",
                project_id="projectId",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_move(self, client: Taskade) -> None:
        task = client.projects.tasks.move(
            task_id="taskId",
            project_id="projectId",
            target={
                "position": "beforebegin",
                "task_id": "x",
            },
        )
        assert_matches_type(TaskMoveResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_move(self, client: Taskade) -> None:
        response = client.projects.tasks.with_raw_response.move(
            task_id="taskId",
            project_id="projectId",
            target={
                "position": "beforebegin",
                "task_id": "x",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskMoveResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_move(self, client: Taskade) -> None:
        with client.projects.tasks.with_streaming_response.move(
            task_id="taskId",
            project_id="projectId",
            target={
                "position": "beforebegin",
                "task_id": "x",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskMoveResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_move(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.tasks.with_raw_response.move(
                task_id="taskId",
                project_id="",
                target={
                    "position": "beforebegin",
                    "task_id": "x",
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.projects.tasks.with_raw_response.move(
                task_id="",
                project_id="projectId",
                target={
                    "position": "beforebegin",
                    "task_id": "x",
                },
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_uncomplete(self, client: Taskade) -> None:
        task = client.projects.tasks.uncomplete(
            task_id="taskId",
            project_id="projectId",
        )
        assert_matches_type(TaskUncompleteResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_uncomplete(self, client: Taskade) -> None:
        response = client.projects.tasks.with_raw_response.uncomplete(
            task_id="taskId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskUncompleteResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_uncomplete(self, client: Taskade) -> None:
        with client.projects.tasks.with_streaming_response.uncomplete(
            task_id="taskId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskUncompleteResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_uncomplete(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.tasks.with_raw_response.uncomplete(
                task_id="taskId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.projects.tasks.with_raw_response.uncomplete(
                task_id="",
                project_id="projectId",
            )


class TestAsyncTasks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncTaskade) -> None:
        task = await async_client.projects.tasks.create(
            project_id="projectId",
            tasks=[{"placement": "afterbegin"}],
        )
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTaskade) -> None:
        response = await async_client.projects.tasks.with_raw_response.create(
            project_id="projectId",
            tasks=[{"placement": "afterbegin"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTaskade) -> None:
        async with async_client.projects.tasks.with_streaming_response.create(
            project_id="projectId",
            tasks=[{"placement": "afterbegin"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskCreateResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.tasks.with_raw_response.create(
                project_id="",
                tasks=[{"placement": "afterbegin"}],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTaskade) -> None:
        task = await async_client.projects.tasks.retrieve(
            task_id="taskId",
            project_id="projectId",
        )
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTaskade) -> None:
        response = await async_client.projects.tasks.with_raw_response.retrieve(
            task_id="taskId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTaskade) -> None:
        async with async_client.projects.tasks.with_streaming_response.retrieve(
            task_id="taskId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskRetrieveResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.tasks.with_raw_response.retrieve(
                task_id="taskId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.projects.tasks.with_raw_response.retrieve(
                task_id="",
                project_id="projectId",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncTaskade) -> None:
        task = await async_client.projects.tasks.update(
            task_id="taskId",
            project_id="projectId",
            content="content",
            content_type="text/markdown",
        )
        assert_matches_type(TaskUpdateResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTaskade) -> None:
        response = await async_client.projects.tasks.with_raw_response.update(
            task_id="taskId",
            project_id="projectId",
            content="content",
            content_type="text/markdown",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskUpdateResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTaskade) -> None:
        async with async_client.projects.tasks.with_streaming_response.update(
            task_id="taskId",
            project_id="projectId",
            content="content",
            content_type="text/markdown",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskUpdateResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.tasks.with_raw_response.update(
                task_id="taskId",
                project_id="",
                content="content",
                content_type="text/markdown",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.projects.tasks.with_raw_response.update(
                task_id="",
                project_id="projectId",
                content="content",
                content_type="text/markdown",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncTaskade) -> None:
        task = await async_client.projects.tasks.list(
            project_id="projectId",
        )
        assert_matches_type(TaskListResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTaskade) -> None:
        task = await async_client.projects.tasks.list(
            project_id="projectId",
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
        )
        assert_matches_type(TaskListResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTaskade) -> None:
        response = await async_client.projects.tasks.with_raw_response.list(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskListResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTaskade) -> None:
        async with async_client.projects.tasks.with_streaming_response.list(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskListResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.tasks.with_raw_response.list(
                project_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncTaskade) -> None:
        task = await async_client.projects.tasks.delete(
            task_id="taskId",
            project_id="projectId",
        )
        assert_matches_type(TaskDeleteResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTaskade) -> None:
        response = await async_client.projects.tasks.with_raw_response.delete(
            task_id="taskId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskDeleteResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTaskade) -> None:
        async with async_client.projects.tasks.with_streaming_response.delete(
            task_id="taskId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskDeleteResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.tasks.with_raw_response.delete(
                task_id="taskId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.projects.tasks.with_raw_response.delete(
                task_id="",
                project_id="projectId",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_complete(self, async_client: AsyncTaskade) -> None:
        task = await async_client.projects.tasks.complete(
            task_id="taskId",
            project_id="projectId",
        )
        assert_matches_type(TaskCompleteResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_complete(self, async_client: AsyncTaskade) -> None:
        response = await async_client.projects.tasks.with_raw_response.complete(
            task_id="taskId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskCompleteResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_complete(self, async_client: AsyncTaskade) -> None:
        async with async_client.projects.tasks.with_streaming_response.complete(
            task_id="taskId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskCompleteResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_complete(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.tasks.with_raw_response.complete(
                task_id="taskId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.projects.tasks.with_raw_response.complete(
                task_id="",
                project_id="projectId",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_move(self, async_client: AsyncTaskade) -> None:
        task = await async_client.projects.tasks.move(
            task_id="taskId",
            project_id="projectId",
            target={
                "position": "beforebegin",
                "task_id": "x",
            },
        )
        assert_matches_type(TaskMoveResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_move(self, async_client: AsyncTaskade) -> None:
        response = await async_client.projects.tasks.with_raw_response.move(
            task_id="taskId",
            project_id="projectId",
            target={
                "position": "beforebegin",
                "task_id": "x",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskMoveResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_move(self, async_client: AsyncTaskade) -> None:
        async with async_client.projects.tasks.with_streaming_response.move(
            task_id="taskId",
            project_id="projectId",
            target={
                "position": "beforebegin",
                "task_id": "x",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskMoveResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_move(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.tasks.with_raw_response.move(
                task_id="taskId",
                project_id="",
                target={
                    "position": "beforebegin",
                    "task_id": "x",
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.projects.tasks.with_raw_response.move(
                task_id="",
                project_id="projectId",
                target={
                    "position": "beforebegin",
                    "task_id": "x",
                },
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_uncomplete(self, async_client: AsyncTaskade) -> None:
        task = await async_client.projects.tasks.uncomplete(
            task_id="taskId",
            project_id="projectId",
        )
        assert_matches_type(TaskUncompleteResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_uncomplete(self, async_client: AsyncTaskade) -> None:
        response = await async_client.projects.tasks.with_raw_response.uncomplete(
            task_id="taskId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskUncompleteResponse, task, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_uncomplete(self, async_client: AsyncTaskade) -> None:
        async with async_client.projects.tasks.with_streaming_response.uncomplete(
            task_id="taskId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskUncompleteResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_uncomplete(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.tasks.with_raw_response.uncomplete(
                task_id="taskId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.projects.tasks.with_raw_response.uncomplete(
                task_id="",
                project_id="projectId",
            )
