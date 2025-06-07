# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from taskade import Taskade, AsyncTaskade
from tests.utils import assert_matches_type
from taskade.types import MeListProjectsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMe:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_projects(self, client: Taskade) -> None:
        me = client.me.list_projects()
        assert_matches_type(MeListProjectsResponse, me, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_projects_with_all_params(self, client: Taskade) -> None:
        me = client.me.list_projects(
            limit=0,
            page=0,
            sort="viewed-asc",
        )
        assert_matches_type(MeListProjectsResponse, me, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_projects(self, client: Taskade) -> None:
        response = client.me.with_raw_response.list_projects()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        me = response.parse()
        assert_matches_type(MeListProjectsResponse, me, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_projects(self, client: Taskade) -> None:
        with client.me.with_streaming_response.list_projects() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            me = response.parse()
            assert_matches_type(MeListProjectsResponse, me, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMe:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_projects(self, async_client: AsyncTaskade) -> None:
        me = await async_client.me.list_projects()
        assert_matches_type(MeListProjectsResponse, me, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_projects_with_all_params(self, async_client: AsyncTaskade) -> None:
        me = await async_client.me.list_projects(
            limit=0,
            page=0,
            sort="viewed-asc",
        )
        assert_matches_type(MeListProjectsResponse, me, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_projects(self, async_client: AsyncTaskade) -> None:
        response = await async_client.me.with_raw_response.list_projects()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        me = await response.parse()
        assert_matches_type(MeListProjectsResponse, me, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_projects(self, async_client: AsyncTaskade) -> None:
        async with async_client.me.with_streaming_response.list_projects() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            me = await response.parse()
            assert_matches_type(MeListProjectsResponse, me, path=["response"])

        assert cast(Any, response.is_closed) is True
