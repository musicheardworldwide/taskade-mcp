# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from taskade import Taskade, AsyncTaskade
from tests.utils import assert_matches_type
from taskade.types.projects.tasks import (
    FieldListResponse,
    FieldDeleteResponse,
    FieldUpdateResponse,
    FieldRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFields:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Taskade) -> None:
        field = client.projects.tasks.fields.retrieve(
            field_id="fieldId",
            project_id="projectId",
            task_id="taskId",
        )
        assert_matches_type(FieldRetrieveResponse, field, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Taskade) -> None:
        response = client.projects.tasks.fields.with_raw_response.retrieve(
            field_id="fieldId",
            project_id="projectId",
            task_id="taskId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = response.parse()
        assert_matches_type(FieldRetrieveResponse, field, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Taskade) -> None:
        with client.projects.tasks.fields.with_streaming_response.retrieve(
            field_id="fieldId",
            project_id="projectId",
            task_id="taskId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = response.parse()
            assert_matches_type(FieldRetrieveResponse, field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.tasks.fields.with_raw_response.retrieve(
                field_id="fieldId",
                project_id="",
                task_id="taskId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.projects.tasks.fields.with_raw_response.retrieve(
                field_id="fieldId",
                project_id="projectId",
                task_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `field_id` but received ''"):
            client.projects.tasks.fields.with_raw_response.retrieve(
                field_id="",
                project_id="projectId",
                task_id="taskId",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Taskade) -> None:
        field = client.projects.tasks.fields.update(
            field_id="fieldId",
            project_id="projectId",
            task_id="taskId",
            value=0,
        )
        assert_matches_type(FieldUpdateResponse, field, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Taskade) -> None:
        response = client.projects.tasks.fields.with_raw_response.update(
            field_id="fieldId",
            project_id="projectId",
            task_id="taskId",
            value=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = response.parse()
        assert_matches_type(FieldUpdateResponse, field, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Taskade) -> None:
        with client.projects.tasks.fields.with_streaming_response.update(
            field_id="fieldId",
            project_id="projectId",
            task_id="taskId",
            value=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = response.parse()
            assert_matches_type(FieldUpdateResponse, field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.tasks.fields.with_raw_response.update(
                field_id="fieldId",
                project_id="",
                task_id="taskId",
                value=0,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.projects.tasks.fields.with_raw_response.update(
                field_id="fieldId",
                project_id="projectId",
                task_id="",
                value=0,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `field_id` but received ''"):
            client.projects.tasks.fields.with_raw_response.update(
                field_id="",
                project_id="projectId",
                task_id="taskId",
                value=0,
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Taskade) -> None:
        field = client.projects.tasks.fields.list(
            task_id="taskId",
            project_id="projectId",
        )
        assert_matches_type(FieldListResponse, field, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Taskade) -> None:
        response = client.projects.tasks.fields.with_raw_response.list(
            task_id="taskId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = response.parse()
        assert_matches_type(FieldListResponse, field, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Taskade) -> None:
        with client.projects.tasks.fields.with_streaming_response.list(
            task_id="taskId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = response.parse()
            assert_matches_type(FieldListResponse, field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.tasks.fields.with_raw_response.list(
                task_id="taskId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.projects.tasks.fields.with_raw_response.list(
                task_id="",
                project_id="projectId",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Taskade) -> None:
        field = client.projects.tasks.fields.delete(
            field_id="fieldId",
            project_id="projectId",
            task_id="taskId",
        )
        assert_matches_type(FieldDeleteResponse, field, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Taskade) -> None:
        response = client.projects.tasks.fields.with_raw_response.delete(
            field_id="fieldId",
            project_id="projectId",
            task_id="taskId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = response.parse()
        assert_matches_type(FieldDeleteResponse, field, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Taskade) -> None:
        with client.projects.tasks.fields.with_streaming_response.delete(
            field_id="fieldId",
            project_id="projectId",
            task_id="taskId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = response.parse()
            assert_matches_type(FieldDeleteResponse, field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.tasks.fields.with_raw_response.delete(
                field_id="fieldId",
                project_id="",
                task_id="taskId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.projects.tasks.fields.with_raw_response.delete(
                field_id="fieldId",
                project_id="projectId",
                task_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `field_id` but received ''"):
            client.projects.tasks.fields.with_raw_response.delete(
                field_id="",
                project_id="projectId",
                task_id="taskId",
            )


class TestAsyncFields:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTaskade) -> None:
        field = await async_client.projects.tasks.fields.retrieve(
            field_id="fieldId",
            project_id="projectId",
            task_id="taskId",
        )
        assert_matches_type(FieldRetrieveResponse, field, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTaskade) -> None:
        response = await async_client.projects.tasks.fields.with_raw_response.retrieve(
            field_id="fieldId",
            project_id="projectId",
            task_id="taskId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = await response.parse()
        assert_matches_type(FieldRetrieveResponse, field, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTaskade) -> None:
        async with async_client.projects.tasks.fields.with_streaming_response.retrieve(
            field_id="fieldId",
            project_id="projectId",
            task_id="taskId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = await response.parse()
            assert_matches_type(FieldRetrieveResponse, field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.tasks.fields.with_raw_response.retrieve(
                field_id="fieldId",
                project_id="",
                task_id="taskId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.projects.tasks.fields.with_raw_response.retrieve(
                field_id="fieldId",
                project_id="projectId",
                task_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `field_id` but received ''"):
            await async_client.projects.tasks.fields.with_raw_response.retrieve(
                field_id="",
                project_id="projectId",
                task_id="taskId",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncTaskade) -> None:
        field = await async_client.projects.tasks.fields.update(
            field_id="fieldId",
            project_id="projectId",
            task_id="taskId",
            value=0,
        )
        assert_matches_type(FieldUpdateResponse, field, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTaskade) -> None:
        response = await async_client.projects.tasks.fields.with_raw_response.update(
            field_id="fieldId",
            project_id="projectId",
            task_id="taskId",
            value=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = await response.parse()
        assert_matches_type(FieldUpdateResponse, field, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTaskade) -> None:
        async with async_client.projects.tasks.fields.with_streaming_response.update(
            field_id="fieldId",
            project_id="projectId",
            task_id="taskId",
            value=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = await response.parse()
            assert_matches_type(FieldUpdateResponse, field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.tasks.fields.with_raw_response.update(
                field_id="fieldId",
                project_id="",
                task_id="taskId",
                value=0,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.projects.tasks.fields.with_raw_response.update(
                field_id="fieldId",
                project_id="projectId",
                task_id="",
                value=0,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `field_id` but received ''"):
            await async_client.projects.tasks.fields.with_raw_response.update(
                field_id="",
                project_id="projectId",
                task_id="taskId",
                value=0,
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncTaskade) -> None:
        field = await async_client.projects.tasks.fields.list(
            task_id="taskId",
            project_id="projectId",
        )
        assert_matches_type(FieldListResponse, field, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTaskade) -> None:
        response = await async_client.projects.tasks.fields.with_raw_response.list(
            task_id="taskId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = await response.parse()
        assert_matches_type(FieldListResponse, field, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTaskade) -> None:
        async with async_client.projects.tasks.fields.with_streaming_response.list(
            task_id="taskId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = await response.parse()
            assert_matches_type(FieldListResponse, field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.tasks.fields.with_raw_response.list(
                task_id="taskId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.projects.tasks.fields.with_raw_response.list(
                task_id="",
                project_id="projectId",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncTaskade) -> None:
        field = await async_client.projects.tasks.fields.delete(
            field_id="fieldId",
            project_id="projectId",
            task_id="taskId",
        )
        assert_matches_type(FieldDeleteResponse, field, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTaskade) -> None:
        response = await async_client.projects.tasks.fields.with_raw_response.delete(
            field_id="fieldId",
            project_id="projectId",
            task_id="taskId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = await response.parse()
        assert_matches_type(FieldDeleteResponse, field, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTaskade) -> None:
        async with async_client.projects.tasks.fields.with_streaming_response.delete(
            field_id="fieldId",
            project_id="projectId",
            task_id="taskId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = await response.parse()
            assert_matches_type(FieldDeleteResponse, field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.tasks.fields.with_raw_response.delete(
                field_id="fieldId",
                project_id="",
                task_id="taskId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.projects.tasks.fields.with_raw_response.delete(
                field_id="fieldId",
                project_id="projectId",
                task_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `field_id` but received ''"):
            await async_client.projects.tasks.fields.with_raw_response.delete(
                field_id="",
                project_id="projectId",
                task_id="taskId",
            )
