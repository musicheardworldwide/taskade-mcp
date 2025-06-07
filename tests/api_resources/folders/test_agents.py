# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from taskade import Taskade, AsyncTaskade
from tests.utils import assert_matches_type
from taskade.types.folders import AgentListResponse, AgentCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Taskade) -> None:
        agent = client.folders.agents.create(
            folder_id="folderId",
            data={
                "data": {
                    "commands": [
                        {
                            "id": "x",
                            "name": "x",
                            "prompt": "x",
                        }
                    ]
                },
                "type": "data",
            },
            name="name",
        )
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Taskade) -> None:
        response = client.folders.agents.with_raw_response.create(
            folder_id="folderId",
            data={
                "data": {
                    "commands": [
                        {
                            "id": "x",
                            "name": "x",
                            "prompt": "x",
                        }
                    ]
                },
                "type": "data",
            },
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Taskade) -> None:
        with client.folders.agents.with_streaming_response.create(
            folder_id="folderId",
            data={
                "data": {
                    "commands": [
                        {
                            "id": "x",
                            "name": "x",
                            "prompt": "x",
                        }
                    ]
                },
                "type": "data",
            },
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentCreateResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.folders.agents.with_raw_response.create(
                folder_id="",
                data={
                    "data": {
                        "commands": [
                            {
                                "id": "x",
                                "name": "x",
                                "prompt": "x",
                            }
                        ]
                    },
                    "type": "data",
                },
                name="name",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Taskade) -> None:
        agent = client.folders.agents.list(
            folder_id="folderId",
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Taskade) -> None:
        agent = client.folders.agents.list(
            folder_id="folderId",
            limit=0,
            page=0,
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Taskade) -> None:
        response = client.folders.agents.with_raw_response.list(
            folder_id="folderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Taskade) -> None:
        with client.folders.agents.with_streaming_response.list(
            folder_id="folderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.folders.agents.with_raw_response.list(
                folder_id="",
            )


class TestAsyncAgents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncTaskade) -> None:
        agent = await async_client.folders.agents.create(
            folder_id="folderId",
            data={
                "data": {
                    "commands": [
                        {
                            "id": "x",
                            "name": "x",
                            "prompt": "x",
                        }
                    ]
                },
                "type": "data",
            },
            name="name",
        )
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTaskade) -> None:
        response = await async_client.folders.agents.with_raw_response.create(
            folder_id="folderId",
            data={
                "data": {
                    "commands": [
                        {
                            "id": "x",
                            "name": "x",
                            "prompt": "x",
                        }
                    ]
                },
                "type": "data",
            },
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTaskade) -> None:
        async with async_client.folders.agents.with_streaming_response.create(
            folder_id="folderId",
            data={
                "data": {
                    "commands": [
                        {
                            "id": "x",
                            "name": "x",
                            "prompt": "x",
                        }
                    ]
                },
                "type": "data",
            },
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentCreateResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.folders.agents.with_raw_response.create(
                folder_id="",
                data={
                    "data": {
                        "commands": [
                            {
                                "id": "x",
                                "name": "x",
                                "prompt": "x",
                            }
                        ]
                    },
                    "type": "data",
                },
                name="name",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncTaskade) -> None:
        agent = await async_client.folders.agents.list(
            folder_id="folderId",
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTaskade) -> None:
        agent = await async_client.folders.agents.list(
            folder_id="folderId",
            limit=0,
            page=0,
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTaskade) -> None:
        response = await async_client.folders.agents.with_raw_response.list(
            folder_id="folderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTaskade) -> None:
        async with async_client.folders.agents.with_streaming_response.list(
            folder_id="folderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.folders.agents.with_raw_response.list(
                folder_id="",
            )
