# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from taskade import Taskade, AsyncTaskade
from tests.utils import assert_matches_type
from taskade.types import (
    AgentDeleteResponse,
    AgentUpdateResponse,
    AgentRetrieveResponse,
    AgentEnablePublicAccessResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Taskade) -> None:
        agent = client.agents.retrieve(
            "agentId",
        )
        assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Taskade) -> None:
        response = client.agents.with_raw_response.retrieve(
            "agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Taskade) -> None:
        with client.agents.with_streaming_response.retrieve(
            "agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Taskade) -> None:
        agent = client.agents.update(
            agent_id="agentId",
        )
        assert_matches_type(AgentUpdateResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Taskade) -> None:
        agent = client.agents.update(
            agent_id="agentId",
            data={
                "commands": [
                    {
                        "id": "x",
                        "name": "x",
                        "prompt": "x",
                        "mode": "default",
                    }
                ],
                "avatar": {
                    "data": {"value": "value"},
                    "type": "emoji",
                },
                "description": "description",
                "input_placeholder": "inputPlaceholder",
                "knowledge_enabled": True,
                "language": "language",
                "tone": "authoritative",
            },
            name="name",
        )
        assert_matches_type(AgentUpdateResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Taskade) -> None:
        response = client.agents.with_raw_response.update(
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentUpdateResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Taskade) -> None:
        with client.agents.with_streaming_response.update(
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentUpdateResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.update(
                agent_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Taskade) -> None:
        agent = client.agents.delete(
            "agentId",
        )
        assert_matches_type(AgentDeleteResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Taskade) -> None:
        response = client.agents.with_raw_response.delete(
            "agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentDeleteResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Taskade) -> None:
        with client.agents.with_streaming_response.delete(
            "agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentDeleteResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_enable_public_access(self, client: Taskade) -> None:
        agent = client.agents.enable_public_access(
            "agentId",
        )
        assert_matches_type(AgentEnablePublicAccessResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_enable_public_access(self, client: Taskade) -> None:
        response = client.agents.with_raw_response.enable_public_access(
            "agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentEnablePublicAccessResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_enable_public_access(self, client: Taskade) -> None:
        with client.agents.with_streaming_response.enable_public_access(
            "agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentEnablePublicAccessResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_enable_public_access(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.enable_public_access(
                "",
            )


class TestAsyncAgents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTaskade) -> None:
        agent = await async_client.agents.retrieve(
            "agentId",
        )
        assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTaskade) -> None:
        response = await async_client.agents.with_raw_response.retrieve(
            "agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTaskade) -> None:
        async with async_client.agents.with_streaming_response.retrieve(
            "agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncTaskade) -> None:
        agent = await async_client.agents.update(
            agent_id="agentId",
        )
        assert_matches_type(AgentUpdateResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTaskade) -> None:
        agent = await async_client.agents.update(
            agent_id="agentId",
            data={
                "commands": [
                    {
                        "id": "x",
                        "name": "x",
                        "prompt": "x",
                        "mode": "default",
                    }
                ],
                "avatar": {
                    "data": {"value": "value"},
                    "type": "emoji",
                },
                "description": "description",
                "input_placeholder": "inputPlaceholder",
                "knowledge_enabled": True,
                "language": "language",
                "tone": "authoritative",
            },
            name="name",
        )
        assert_matches_type(AgentUpdateResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTaskade) -> None:
        response = await async_client.agents.with_raw_response.update(
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentUpdateResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTaskade) -> None:
        async with async_client.agents.with_streaming_response.update(
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentUpdateResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.update(
                agent_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncTaskade) -> None:
        agent = await async_client.agents.delete(
            "agentId",
        )
        assert_matches_type(AgentDeleteResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTaskade) -> None:
        response = await async_client.agents.with_raw_response.delete(
            "agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentDeleteResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTaskade) -> None:
        async with async_client.agents.with_streaming_response.delete(
            "agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentDeleteResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_enable_public_access(self, async_client: AsyncTaskade) -> None:
        agent = await async_client.agents.enable_public_access(
            "agentId",
        )
        assert_matches_type(AgentEnablePublicAccessResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_enable_public_access(self, async_client: AsyncTaskade) -> None:
        response = await async_client.agents.with_raw_response.enable_public_access(
            "agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentEnablePublicAccessResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_enable_public_access(self, async_client: AsyncTaskade) -> None:
        async with async_client.agents.with_streaming_response.enable_public_access(
            "agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentEnablePublicAccessResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_enable_public_access(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.enable_public_access(
                "",
            )
