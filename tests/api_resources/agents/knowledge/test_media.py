# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from taskade import Taskade, AsyncTaskade
from tests.utils import assert_matches_type
from taskade.types.agents.knowledge import MediaCreateResponse, MediaDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMedia:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Taskade) -> None:
        media = client.agents.knowledge.media.create(
            agent_id="agentId",
            media_id="mediaId",
        )
        assert_matches_type(MediaCreateResponse, media, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Taskade) -> None:
        response = client.agents.knowledge.media.with_raw_response.create(
            agent_id="agentId",
            media_id="mediaId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = response.parse()
        assert_matches_type(MediaCreateResponse, media, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Taskade) -> None:
        with client.agents.knowledge.media.with_streaming_response.create(
            agent_id="agentId",
            media_id="mediaId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = response.parse()
            assert_matches_type(MediaCreateResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.knowledge.media.with_raw_response.create(
                agent_id="",
                media_id="mediaId",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Taskade) -> None:
        media = client.agents.knowledge.media.delete(
            media_id="mediaId",
            agent_id="agentId",
        )
        assert_matches_type(MediaDeleteResponse, media, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Taskade) -> None:
        response = client.agents.knowledge.media.with_raw_response.delete(
            media_id="mediaId",
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = response.parse()
        assert_matches_type(MediaDeleteResponse, media, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Taskade) -> None:
        with client.agents.knowledge.media.with_streaming_response.delete(
            media_id="mediaId",
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = response.parse()
            assert_matches_type(MediaDeleteResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.knowledge.media.with_raw_response.delete(
                media_id="mediaId",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `media_id` but received ''"):
            client.agents.knowledge.media.with_raw_response.delete(
                media_id="",
                agent_id="agentId",
            )


class TestAsyncMedia:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncTaskade) -> None:
        media = await async_client.agents.knowledge.media.create(
            agent_id="agentId",
            media_id="mediaId",
        )
        assert_matches_type(MediaCreateResponse, media, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTaskade) -> None:
        response = await async_client.agents.knowledge.media.with_raw_response.create(
            agent_id="agentId",
            media_id="mediaId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = await response.parse()
        assert_matches_type(MediaCreateResponse, media, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTaskade) -> None:
        async with async_client.agents.knowledge.media.with_streaming_response.create(
            agent_id="agentId",
            media_id="mediaId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = await response.parse()
            assert_matches_type(MediaCreateResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.knowledge.media.with_raw_response.create(
                agent_id="",
                media_id="mediaId",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncTaskade) -> None:
        media = await async_client.agents.knowledge.media.delete(
            media_id="mediaId",
            agent_id="agentId",
        )
        assert_matches_type(MediaDeleteResponse, media, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTaskade) -> None:
        response = await async_client.agents.knowledge.media.with_raw_response.delete(
            media_id="mediaId",
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = await response.parse()
        assert_matches_type(MediaDeleteResponse, media, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTaskade) -> None:
        async with async_client.agents.knowledge.media.with_streaming_response.delete(
            media_id="mediaId",
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = await response.parse()
            assert_matches_type(MediaDeleteResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.knowledge.media.with_raw_response.delete(
                media_id="mediaId",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `media_id` but received ''"):
            await async_client.agents.knowledge.media.with_raw_response.delete(
                media_id="",
                agent_id="agentId",
            )
