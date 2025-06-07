# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from taskade import Taskade, AsyncTaskade
from tests.utils import assert_matches_type
from taskade.types import PublicAgentRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPublicAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Taskade) -> None:
        public_agent = client.public_agents.retrieve(
            "publicAgentId",
        )
        assert_matches_type(PublicAgentRetrieveResponse, public_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Taskade) -> None:
        response = client.public_agents.with_raw_response.retrieve(
            "publicAgentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        public_agent = response.parse()
        assert_matches_type(PublicAgentRetrieveResponse, public_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Taskade) -> None:
        with client.public_agents.with_streaming_response.retrieve(
            "publicAgentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            public_agent = response.parse()
            assert_matches_type(PublicAgentRetrieveResponse, public_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `public_agent_id` but received ''"):
            client.public_agents.with_raw_response.retrieve(
                "",
            )


class TestAsyncPublicAgents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTaskade) -> None:
        public_agent = await async_client.public_agents.retrieve(
            "publicAgentId",
        )
        assert_matches_type(PublicAgentRetrieveResponse, public_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTaskade) -> None:
        response = await async_client.public_agents.with_raw_response.retrieve(
            "publicAgentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        public_agent = await response.parse()
        assert_matches_type(PublicAgentRetrieveResponse, public_agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTaskade) -> None:
        async with async_client.public_agents.with_streaming_response.retrieve(
            "publicAgentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            public_agent = await response.parse()
            assert_matches_type(PublicAgentRetrieveResponse, public_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `public_agent_id` but received ''"):
            await async_client.public_agents.with_raw_response.retrieve(
                "",
            )
