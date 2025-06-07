# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from taskade import Taskade, AsyncTaskade
from tests.utils import assert_matches_type
from taskade.types.projects.tasks import (
    DateDeleteResponse,
    DateUpdateResponse,
    DateRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Taskade) -> None:
        date = client.projects.tasks.date.retrieve(
            task_id="taskId",
            project_id="projectId",
        )
        assert_matches_type(DateRetrieveResponse, date, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Taskade) -> None:
        response = client.projects.tasks.date.with_raw_response.retrieve(
            task_id="taskId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        date = response.parse()
        assert_matches_type(DateRetrieveResponse, date, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Taskade) -> None:
        with client.projects.tasks.date.with_streaming_response.retrieve(
            task_id="taskId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            date = response.parse()
            assert_matches_type(DateRetrieveResponse, date, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.tasks.date.with_raw_response.retrieve(
                task_id="taskId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.projects.tasks.date.with_raw_response.retrieve(
                task_id="",
                project_id="projectId",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Taskade) -> None:
        date = client.projects.tasks.date.update(
            task_id="taskId",
            project_id="projectId",
            start={"date": "7321-69-10"},
        )
        assert_matches_type(DateUpdateResponse, date, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Taskade) -> None:
        date = client.projects.tasks.date.update(
            task_id="taskId",
            project_id="projectId",
            start={
                "date": "7321-69-10",
                "time": "20:56",
                "timezone": "timezone",
            },
            end={
                "date": "7321-69-10",
                "time": "20:56",
                "timezone": "timezone",
            },
        )
        assert_matches_type(DateUpdateResponse, date, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Taskade) -> None:
        response = client.projects.tasks.date.with_raw_response.update(
            task_id="taskId",
            project_id="projectId",
            start={"date": "7321-69-10"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        date = response.parse()
        assert_matches_type(DateUpdateResponse, date, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Taskade) -> None:
        with client.projects.tasks.date.with_streaming_response.update(
            task_id="taskId",
            project_id="projectId",
            start={"date": "7321-69-10"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            date = response.parse()
            assert_matches_type(DateUpdateResponse, date, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.tasks.date.with_raw_response.update(
                task_id="taskId",
                project_id="",
                start={"date": "7321-69-10"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.projects.tasks.date.with_raw_response.update(
                task_id="",
                project_id="projectId",
                start={"date": "7321-69-10"},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Taskade) -> None:
        date = client.projects.tasks.date.delete(
            task_id="taskId",
            project_id="projectId",
        )
        assert_matches_type(DateDeleteResponse, date, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Taskade) -> None:
        response = client.projects.tasks.date.with_raw_response.delete(
            task_id="taskId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        date = response.parse()
        assert_matches_type(DateDeleteResponse, date, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Taskade) -> None:
        with client.projects.tasks.date.with_streaming_response.delete(
            task_id="taskId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            date = response.parse()
            assert_matches_type(DateDeleteResponse, date, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.tasks.date.with_raw_response.delete(
                task_id="taskId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.projects.tasks.date.with_raw_response.delete(
                task_id="",
                project_id="projectId",
            )


class TestAsyncDate:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTaskade) -> None:
        date = await async_client.projects.tasks.date.retrieve(
            task_id="taskId",
            project_id="projectId",
        )
        assert_matches_type(DateRetrieveResponse, date, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTaskade) -> None:
        response = await async_client.projects.tasks.date.with_raw_response.retrieve(
            task_id="taskId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        date = await response.parse()
        assert_matches_type(DateRetrieveResponse, date, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTaskade) -> None:
        async with async_client.projects.tasks.date.with_streaming_response.retrieve(
            task_id="taskId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            date = await response.parse()
            assert_matches_type(DateRetrieveResponse, date, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.tasks.date.with_raw_response.retrieve(
                task_id="taskId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.projects.tasks.date.with_raw_response.retrieve(
                task_id="",
                project_id="projectId",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncTaskade) -> None:
        date = await async_client.projects.tasks.date.update(
            task_id="taskId",
            project_id="projectId",
            start={"date": "7321-69-10"},
        )
        assert_matches_type(DateUpdateResponse, date, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTaskade) -> None:
        date = await async_client.projects.tasks.date.update(
            task_id="taskId",
            project_id="projectId",
            start={
                "date": "7321-69-10",
                "time": "20:56",
                "timezone": "timezone",
            },
            end={
                "date": "7321-69-10",
                "time": "20:56",
                "timezone": "timezone",
            },
        )
        assert_matches_type(DateUpdateResponse, date, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTaskade) -> None:
        response = await async_client.projects.tasks.date.with_raw_response.update(
            task_id="taskId",
            project_id="projectId",
            start={"date": "7321-69-10"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        date = await response.parse()
        assert_matches_type(DateUpdateResponse, date, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTaskade) -> None:
        async with async_client.projects.tasks.date.with_streaming_response.update(
            task_id="taskId",
            project_id="projectId",
            start={"date": "7321-69-10"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            date = await response.parse()
            assert_matches_type(DateUpdateResponse, date, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.tasks.date.with_raw_response.update(
                task_id="taskId",
                project_id="",
                start={"date": "7321-69-10"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.projects.tasks.date.with_raw_response.update(
                task_id="",
                project_id="projectId",
                start={"date": "7321-69-10"},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncTaskade) -> None:
        date = await async_client.projects.tasks.date.delete(
            task_id="taskId",
            project_id="projectId",
        )
        assert_matches_type(DateDeleteResponse, date, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTaskade) -> None:
        response = await async_client.projects.tasks.date.with_raw_response.delete(
            task_id="taskId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        date = await response.parse()
        assert_matches_type(DateDeleteResponse, date, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTaskade) -> None:
        async with async_client.projects.tasks.date.with_streaming_response.delete(
            task_id="taskId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            date = await response.parse()
            assert_matches_type(DateDeleteResponse, date, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.tasks.date.with_raw_response.delete(
                task_id="taskId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.projects.tasks.date.with_raw_response.delete(
                task_id="",
                project_id="projectId",
            )
