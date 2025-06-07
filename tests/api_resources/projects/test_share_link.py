# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from taskade import Taskade, AsyncTaskade
from tests.utils import assert_matches_type
from taskade.types.projects import ShareLinkEnableResponse, ShareLinkRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestShareLink:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Taskade) -> None:
        share_link = client.projects.share_link.retrieve(
            "projectId",
        )
        assert_matches_type(ShareLinkRetrieveResponse, share_link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Taskade) -> None:
        response = client.projects.share_link.with_raw_response.retrieve(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        share_link = response.parse()
        assert_matches_type(ShareLinkRetrieveResponse, share_link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Taskade) -> None:
        with client.projects.share_link.with_streaming_response.retrieve(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            share_link = response.parse()
            assert_matches_type(ShareLinkRetrieveResponse, share_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.share_link.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_enable(self, client: Taskade) -> None:
        share_link = client.projects.share_link.enable(
            "projectId",
        )
        assert_matches_type(ShareLinkEnableResponse, share_link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_enable(self, client: Taskade) -> None:
        response = client.projects.share_link.with_raw_response.enable(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        share_link = response.parse()
        assert_matches_type(ShareLinkEnableResponse, share_link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_enable(self, client: Taskade) -> None:
        with client.projects.share_link.with_streaming_response.enable(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            share_link = response.parse()
            assert_matches_type(ShareLinkEnableResponse, share_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_enable(self, client: Taskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.share_link.with_raw_response.enable(
                "",
            )


class TestAsyncShareLink:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTaskade) -> None:
        share_link = await async_client.projects.share_link.retrieve(
            "projectId",
        )
        assert_matches_type(ShareLinkRetrieveResponse, share_link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTaskade) -> None:
        response = await async_client.projects.share_link.with_raw_response.retrieve(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        share_link = await response.parse()
        assert_matches_type(ShareLinkRetrieveResponse, share_link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTaskade) -> None:
        async with async_client.projects.share_link.with_streaming_response.retrieve(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            share_link = await response.parse()
            assert_matches_type(ShareLinkRetrieveResponse, share_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.share_link.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_enable(self, async_client: AsyncTaskade) -> None:
        share_link = await async_client.projects.share_link.enable(
            "projectId",
        )
        assert_matches_type(ShareLinkEnableResponse, share_link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_enable(self, async_client: AsyncTaskade) -> None:
        response = await async_client.projects.share_link.with_raw_response.enable(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        share_link = await response.parse()
        assert_matches_type(ShareLinkEnableResponse, share_link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_enable(self, async_client: AsyncTaskade) -> None:
        async with async_client.projects.share_link.with_streaming_response.enable(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            share_link = await response.parse()
            assert_matches_type(ShareLinkEnableResponse, share_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_enable(self, async_client: AsyncTaskade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.share_link.with_raw_response.enable(
                "",
            )
