# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from taskade import Taskade, AsyncTaskade
from tests.utils import assert_matches_type
from taskade.types.agents import PublicAgentUpdateResponse, PublicAgentRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPublicAgent:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Taskade) -> None:
        public_agent = client.agents.public_agent.retrieve(
            "agentId",
        )
        assert_matches_type(PublicAgentRetrieveResponse, public_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Taskade) -> None:
        response = client.agents.public_agent.with_raw_response.retrieve(
            "agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        public_agent = response.parse()
        assert_matches_type(PublicAgentRetrieveResponse, public_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Taskade) -> None:
        with client.agents.public_agent.with_streaming_response.retrieve(
            "agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            public_agent = response.parse()
            assert_matches_type(PublicAgentRetrieveResponse, public_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.public_agent.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Taskade) -> None:
        public_agent = client.agents.public_agent.update(
            agent_id="agentId",
            preferences={},
        )
        assert_matches_type(PublicAgentUpdateResponse, public_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Taskade) -> None:
        public_agent = client.agents.public_agent.update(
            agent_id="agentId",
            preferences={
                "auto_end_chats": True,
                "can_copy_knowledge": True,
                "hide_branding": True,
                "meta": {
                    "description": "description",
                    "image": {
                        "id": "id",
                        "extension": "extension",
                        "mimetype": "mimetype",
                        "namespace": "namespace",
                        "owner_id": "ownerID",
                        "s3_key_original": "s3KeyOriginal",
                        "size": 0,
                        "description": "description",
                        "document_id": "x",
                        "metadata": {"foo": "bar"},
                        "name": "name",
                        "node_id": "x",
                        "owner_type": "x",
                        "space_id": "x",
                        "type": "type",
                        "user_id": 0,
                    },
                    "title": "title",
                },
                "mode": "template",
                "theme": "light",
            },
        )
        assert_matches_type(PublicAgentUpdateResponse, public_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Taskade) -> None:
        response = client.agents.public_agent.with_raw_response.update(
            agent_id="agentId",
            preferences={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        public_agent = response.parse()
        assert_matches_type(PublicAgentUpdateResponse, public_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Taskade) -> None:
        with client.agents.public_agent.with_streaming_response.update(
            agent_id="agentId",
            preferences={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            public_agent = response.parse()
            assert_matches_type(PublicAgentUpdateResponse, public_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.public_agent.with_raw_response.update(
                agent_id="",
                preferences={},
            )


class TestAsyncPublicAgent:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTaskade) -> None:
        public_agent = await async_client.agents.public_agent.retrieve(
            "agentId",
        )
        assert_matches_type(PublicAgentRetrieveResponse, public_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTaskade) -> None:
        response = await async_client.agents.public_agent.with_raw_response.retrieve(
            "agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        public_agent = await response.parse()
        assert_matches_type(PublicAgentRetrieveResponse, public_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTaskade) -> None:
        async with async_client.agents.public_agent.with_streaming_response.retrieve(
            "agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            public_agent = await response.parse()
            assert_matches_type(PublicAgentRetrieveResponse, public_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.public_agent.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncTaskade) -> None:
        public_agent = await async_client.agents.public_agent.update(
            agent_id="agentId",
            preferences={},
        )
        assert_matches_type(PublicAgentUpdateResponse, public_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTaskade) -> None:
        public_agent = await async_client.agents.public_agent.update(
            agent_id="agentId",
            preferences={
                "auto_end_chats": True,
                "can_copy_knowledge": True,
                "hide_branding": True,
                "meta": {
                    "description": "description",
                    "image": {
                        "id": "id",
                        "extension": "extension",
                        "mimetype": "mimetype",
                        "namespace": "namespace",
                        "owner_id": "ownerID",
                        "s3_key_original": "s3KeyOriginal",
                        "size": 0,
                        "description": "description",
                        "document_id": "x",
                        "metadata": {"foo": "bar"},
                        "name": "name",
                        "node_id": "x",
                        "owner_type": "x",
                        "space_id": "x",
                        "type": "type",
                        "user_id": 0,
                    },
                    "title": "title",
                },
                "mode": "template",
                "theme": "light",
            },
        )
        assert_matches_type(PublicAgentUpdateResponse, public_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTaskade) -> None:
        response = await async_client.agents.public_agent.with_raw_response.update(
            agent_id="agentId",
            preferences={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        public_agent = await response.parse()
        assert_matches_type(PublicAgentUpdateResponse, public_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTaskade) -> None:
        async with async_client.agents.public_agent.with_streaming_response.update(
            agent_id="agentId",
            preferences={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            public_agent = await response.parse()
            assert_matches_type(PublicAgentUpdateResponse, public_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.public_agent.with_raw_response.update(
                agent_id="",
                preferences={},
            )
