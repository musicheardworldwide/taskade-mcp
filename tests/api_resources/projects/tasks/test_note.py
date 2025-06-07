# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from taskade import Taskade, AsyncTaskade
from tests.utils import assert_matches_type
from taskade.types.projects.tasks import (
    NoteDeleteResponse,
    NoteUpdateResponse,
    NoteRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNote:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Taskade) -> None:
        note = client.projects.tasks.note.retrieve(
            task_id="taskId",
            project_id="projectId",
        )
        assert_matches_type(NoteRetrieveResponse, note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Taskade) -> None:
        response = client.projects.tasks.note.with_raw_response.retrieve(
            task_id="taskId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = response.parse()
        assert_matches_type(NoteRetrieveResponse, note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Taskade) -> None:
        with client.projects.tasks.note.with_streaming_response.retrieve(
            task_id="taskId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = response.parse()
            assert_matches_type(NoteRetrieveResponse, note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.tasks.note.with_raw_response.retrieve(
                task_id="taskId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.projects.tasks.note.with_raw_response.retrieve(
                task_id="",
                project_id="projectId",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Taskade) -> None:
        note = client.projects.tasks.note.update(
            task_id="taskId",
            project_id="projectId",
            type="text/plain",
            value="value",
        )
        assert_matches_type(NoteUpdateResponse, note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Taskade) -> None:
        response = client.projects.tasks.note.with_raw_response.update(
            task_id="taskId",
            project_id="projectId",
            type="text/plain",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = response.parse()
        assert_matches_type(NoteUpdateResponse, note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Taskade) -> None:
        with client.projects.tasks.note.with_streaming_response.update(
            task_id="taskId",
            project_id="projectId",
            type="text/plain",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = response.parse()
            assert_matches_type(NoteUpdateResponse, note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.tasks.note.with_raw_response.update(
                task_id="taskId",
                project_id="",
                type="text/plain",
                value="value",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.projects.tasks.note.with_raw_response.update(
                task_id="",
                project_id="projectId",
                type="text/plain",
                value="value",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Taskade) -> None:
        note = client.projects.tasks.note.delete(
            task_id="taskId",
            project_id="projectId",
        )
        assert_matches_type(NoteDeleteResponse, note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Taskade) -> None:
        response = client.projects.tasks.note.with_raw_response.delete(
            task_id="taskId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = response.parse()
        assert_matches_type(NoteDeleteResponse, note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Taskade) -> None:
        with client.projects.tasks.note.with_streaming_response.delete(
            task_id="taskId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = response.parse()
            assert_matches_type(NoteDeleteResponse, note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.tasks.note.with_raw_response.delete(
                task_id="taskId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.projects.tasks.note.with_raw_response.delete(
                task_id="",
                project_id="projectId",
            )


class TestAsyncNote:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTaskade) -> None:
        note = await async_client.projects.tasks.note.retrieve(
            task_id="taskId",
            project_id="projectId",
        )
        assert_matches_type(NoteRetrieveResponse, note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTaskade) -> None:
        response = await async_client.projects.tasks.note.with_raw_response.retrieve(
            task_id="taskId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = await response.parse()
        assert_matches_type(NoteRetrieveResponse, note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTaskade) -> None:
        async with async_client.projects.tasks.note.with_streaming_response.retrieve(
            task_id="taskId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = await response.parse()
            assert_matches_type(NoteRetrieveResponse, note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.tasks.note.with_raw_response.retrieve(
                task_id="taskId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.projects.tasks.note.with_raw_response.retrieve(
                task_id="",
                project_id="projectId",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncTaskade) -> None:
        note = await async_client.projects.tasks.note.update(
            task_id="taskId",
            project_id="projectId",
            type="text/plain",
            value="value",
        )
        assert_matches_type(NoteUpdateResponse, note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTaskade) -> None:
        response = await async_client.projects.tasks.note.with_raw_response.update(
            task_id="taskId",
            project_id="projectId",
            type="text/plain",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = await response.parse()
        assert_matches_type(NoteUpdateResponse, note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTaskade) -> None:
        async with async_client.projects.tasks.note.with_streaming_response.update(
            task_id="taskId",
            project_id="projectId",
            type="text/plain",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = await response.parse()
            assert_matches_type(NoteUpdateResponse, note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.tasks.note.with_raw_response.update(
                task_id="taskId",
                project_id="",
                type="text/plain",
                value="value",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.projects.tasks.note.with_raw_response.update(
                task_id="",
                project_id="projectId",
                type="text/plain",
                value="value",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncTaskade) -> None:
        note = await async_client.projects.tasks.note.delete(
            task_id="taskId",
            project_id="projectId",
        )
        assert_matches_type(NoteDeleteResponse, note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTaskade) -> None:
        response = await async_client.projects.tasks.note.with_raw_response.delete(
            task_id="taskId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = await response.parse()
        assert_matches_type(NoteDeleteResponse, note, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTaskade) -> None:
        async with async_client.projects.tasks.note.with_streaming_response.delete(
            task_id="taskId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = await response.parse()
            assert_matches_type(NoteDeleteResponse, note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.tasks.note.with_raw_response.delete(
                task_id="taskId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.projects.tasks.note.with_raw_response.delete(
                task_id="",
                project_id="projectId",
            )
