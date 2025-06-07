# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .convos import (
    ConvosResource,
    AsyncConvosResource,
    ConvosResourceWithRawResponse,
    AsyncConvosResourceWithRawResponse,
    ConvosResourceWithStreamingResponse,
    AsyncConvosResourceWithStreamingResponse,
)
from ...types import agent_update_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .public_agent import (
    PublicAgentResource,
    AsyncPublicAgentResource,
    PublicAgentResourceWithRawResponse,
    AsyncPublicAgentResourceWithRawResponse,
    PublicAgentResourceWithStreamingResponse,
    AsyncPublicAgentResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .knowledge.knowledge import (
    KnowledgeResource,
    AsyncKnowledgeResource,
    KnowledgeResourceWithRawResponse,
    AsyncKnowledgeResourceWithRawResponse,
    KnowledgeResourceWithStreamingResponse,
    AsyncKnowledgeResourceWithStreamingResponse,
)
from ...types.agent_delete_response import AgentDeleteResponse
from ...types.agent_update_response import AgentUpdateResponse
from ...types.agent_retrieve_response import AgentRetrieveResponse
from ...types.agent_enable_public_access_response import AgentEnablePublicAccessResponse

__all__ = ["AgentsResource", "AsyncAgentsResource"]


class AgentsResource(SyncAPIResource):
    @cached_property
    def public_agent(self) -> PublicAgentResource:
        return PublicAgentResource(self._client)

    @cached_property
    def knowledge(self) -> KnowledgeResource:
        return KnowledgeResource(self._client)

    @cached_property
    def convos(self) -> ConvosResource:
        return ConvosResource(self._client)

    @cached_property
    def with_raw_response(self) -> AgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/musicheardworldwide/taskade-mcp#accessing-raw-response-data-eg-headers
        """
        return AgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/musicheardworldwide/taskade-mcp#with_streaming_response
        """
        return AgentsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentRetrieveResponse:
        """
        Get agent with id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRetrieveResponse,
        )

    def update(
        self,
        agent_id: str,
        *,
        data: agent_update_params.Data | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentUpdateResponse:
        """
        Update agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._patch(
            f"/agents/{agent_id}",
            body=maybe_transform(
                {
                    "data": data,
                    "name": name,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentUpdateResponse,
        )

    def delete(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentDeleteResponse:
        """
        Delete an agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._delete(
            f"/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentDeleteResponse,
        )

    def enable_public_access(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentEnablePublicAccessResponse:
        """
        Enable public access in the agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._put(
            f"/agents/{agent_id}/publicAccess",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentEnablePublicAccessResponse,
        )


class AsyncAgentsResource(AsyncAPIResource):
    @cached_property
    def public_agent(self) -> AsyncPublicAgentResource:
        return AsyncPublicAgentResource(self._client)

    @cached_property
    def knowledge(self) -> AsyncKnowledgeResource:
        return AsyncKnowledgeResource(self._client)

    @cached_property
    def convos(self) -> AsyncConvosResource:
        return AsyncConvosResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/musicheardworldwide/taskade-mcp#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/musicheardworldwide/taskade-mcp#with_streaming_response
        """
        return AsyncAgentsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentRetrieveResponse:
        """
        Get agent with id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRetrieveResponse,
        )

    async def update(
        self,
        agent_id: str,
        *,
        data: agent_update_params.Data | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentUpdateResponse:
        """
        Update agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._patch(
            f"/agents/{agent_id}",
            body=await async_maybe_transform(
                {
                    "data": data,
                    "name": name,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentUpdateResponse,
        )

    async def delete(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentDeleteResponse:
        """
        Delete an agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._delete(
            f"/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentDeleteResponse,
        )

    async def enable_public_access(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentEnablePublicAccessResponse:
        """
        Enable public access in the agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._put(
            f"/agents/{agent_id}/publicAccess",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentEnablePublicAccessResponse,
        )


class AgentsResourceWithRawResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.retrieve = to_raw_response_wrapper(
            agents.retrieve,
        )
        self.update = to_raw_response_wrapper(
            agents.update,
        )
        self.delete = to_raw_response_wrapper(
            agents.delete,
        )
        self.enable_public_access = to_raw_response_wrapper(
            agents.enable_public_access,
        )

    @cached_property
    def public_agent(self) -> PublicAgentResourceWithRawResponse:
        return PublicAgentResourceWithRawResponse(self._agents.public_agent)

    @cached_property
    def knowledge(self) -> KnowledgeResourceWithRawResponse:
        return KnowledgeResourceWithRawResponse(self._agents.knowledge)

    @cached_property
    def convos(self) -> ConvosResourceWithRawResponse:
        return ConvosResourceWithRawResponse(self._agents.convos)


class AsyncAgentsResourceWithRawResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.retrieve = async_to_raw_response_wrapper(
            agents.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            agents.update,
        )
        self.delete = async_to_raw_response_wrapper(
            agents.delete,
        )
        self.enable_public_access = async_to_raw_response_wrapper(
            agents.enable_public_access,
        )

    @cached_property
    def public_agent(self) -> AsyncPublicAgentResourceWithRawResponse:
        return AsyncPublicAgentResourceWithRawResponse(self._agents.public_agent)

    @cached_property
    def knowledge(self) -> AsyncKnowledgeResourceWithRawResponse:
        return AsyncKnowledgeResourceWithRawResponse(self._agents.knowledge)

    @cached_property
    def convos(self) -> AsyncConvosResourceWithRawResponse:
        return AsyncConvosResourceWithRawResponse(self._agents.convos)


class AgentsResourceWithStreamingResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.retrieve = to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            agents.update,
        )
        self.delete = to_streamed_response_wrapper(
            agents.delete,
        )
        self.enable_public_access = to_streamed_response_wrapper(
            agents.enable_public_access,
        )

    @cached_property
    def public_agent(self) -> PublicAgentResourceWithStreamingResponse:
        return PublicAgentResourceWithStreamingResponse(self._agents.public_agent)

    @cached_property
    def knowledge(self) -> KnowledgeResourceWithStreamingResponse:
        return KnowledgeResourceWithStreamingResponse(self._agents.knowledge)

    @cached_property
    def convos(self) -> ConvosResourceWithStreamingResponse:
        return ConvosResourceWithStreamingResponse(self._agents.convos)


class AsyncAgentsResourceWithStreamingResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.retrieve = async_to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            agents.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            agents.delete,
        )
        self.enable_public_access = async_to_streamed_response_wrapper(
            agents.enable_public_access,
        )

    @cached_property
    def public_agent(self) -> AsyncPublicAgentResourceWithStreamingResponse:
        return AsyncPublicAgentResourceWithStreamingResponse(self._agents.public_agent)

    @cached_property
    def knowledge(self) -> AsyncKnowledgeResourceWithStreamingResponse:
        return AsyncKnowledgeResourceWithStreamingResponse(self._agents.knowledge)

    @cached_property
    def convos(self) -> AsyncConvosResourceWithStreamingResponse:
        return AsyncConvosResourceWithStreamingResponse(self._agents.convos)
