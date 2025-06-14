# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from taskade import Taskade, AsyncTaskade
from tests.utils import assert_matches_type
from taskade.types.agents import ConvoListResponse, ConvoRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConvos:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Taskade) -> None:
        convo = client.agents.convos.retrieve(
            convo_id="convoId",
            agent_id="agentId",
        )
        assert_matches_type(ConvoRetrieveResponse, convo, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Taskade) -> None:
        response = client.agents.convos.with_raw_response.retrieve(
            convo_id="convoId",
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        convo = response.parse()
        assert_matches_type(ConvoRetrieveResponse, convo, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Taskade) -> None:
        with client.agents.convos.with_streaming_response.retrieve(
            convo_id="convoId",
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            convo = response.parse()
            assert_matches_type(ConvoRetrieveResponse, convo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.convos.with_raw_response.retrieve(
                convo_id="convoId",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `convo_id` but received ''"):
            client.agents.convos.with_raw_response.retrieve(
                convo_id="",
                agent_id="agentId",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Taskade) -> None:
        convo = client.agents.convos.list(
            agent_id="agentId",
        )
        assert_matches_type(ConvoListResponse, convo, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Taskade) -> None:
        convo = client.agents.convos.list(
            agent_id="agentId",
            limit=0,
            page=0,
        )
        assert_matches_type(ConvoListResponse, convo, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Taskade) -> None:
        response = client.agents.convos.with_raw_response.list(
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        convo = response.parse()
        assert_matches_type(ConvoListResponse, convo, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Taskade) -> None:
        with client.agents.convos.with_streaming_response.list(
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            convo = response.parse()
            assert_matches_type(ConvoListResponse, convo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.convos.with_raw_response.list(
                agent_id="",
            )


class TestAsyncConvos:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTaskade) -> None:
        convo = await async_client.agents.convos.retrieve(
            convo_id="convoId",
            agent_id="agentId",
        )
        assert_matches_type(ConvoRetrieveResponse, convo, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTaskade) -> None:
        response = await async_client.agents.convos.with_raw_response.retrieve(
            convo_id="convoId",
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        convo = await response.parse()
        assert_matches_type(ConvoRetrieveResponse, convo, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTaskade) -> None:
        async with async_client.agents.convos.with_streaming_response.retrieve(
            convo_id="convoId",
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            convo = await response.parse()
            assert_matches_type(ConvoRetrieveResponse, convo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.convos.with_raw_response.retrieve(
                convo_id="convoId",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `convo_id` but received ''"):
            await async_client.agents.convos.with_raw_response.retrieve(
                convo_id="",
                agent_id="agentId",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncTaskade) -> None:
        convo = await async_client.agents.convos.list(
            agent_id="agentId",
        )
        assert_matches_type(ConvoListResponse, convo, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTaskade) -> None:
        convo = await async_client.agents.convos.list(
            agent_id="agentId",
            limit=0,
            page=0,
        )
        assert_matches_type(ConvoListResponse, convo, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTaskade) -> None:
        response = await async_client.agents.convos.with_raw_response.list(
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        convo = await response.parse()
        assert_matches_type(ConvoListResponse, convo, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTaskade) -> None:
        async with async_client.agents.convos.with_streaming_response.list(
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            convo = await response.parse()
            assert_matches_type(ConvoListResponse, convo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.convos.with_raw_response.list(
                agent_id="",
            )
