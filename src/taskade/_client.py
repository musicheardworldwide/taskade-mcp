# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import me, medias, workspaces, public_agents
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import TaskadeError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.agents import agents
from .resources.folders import folders
from .resources.projects import projects

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Taskade", "AsyncTaskade", "Client", "AsyncClient"]


class Taskade(SyncAPIClient):
    workspaces: workspaces.WorkspacesResource
    projects: projects.ProjectsResource
    folders: folders.FoldersResource
    me: me.MeResource
    agents: agents.AgentsResource
    medias: medias.MediasResource
    public_agents: public_agents.PublicAgentsResource
    with_raw_response: TaskadeWithRawResponse
    with_streaming_response: TaskadeWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Taskade client instance.

        This automatically infers the `api_key` argument from the `TASKADE_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("TASKADE_API_KEY")
        if api_key is None:
            raise TaskadeError(
                "The api_key client option must be set either by passing api_key to the client or by setting the TASKADE_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("TASKADE_BASE_URL")
        if base_url is None:
            base_url = f"https://www.taskade.com/api/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.workspaces = workspaces.WorkspacesResource(self)
        self.projects = projects.ProjectsResource(self)
        self.folders = folders.FoldersResource(self)
        self.me = me.MeResource(self)
        self.agents = agents.AgentsResource(self)
        self.medias = medias.MediasResource(self)
        self.public_agents = public_agents.PublicAgentsResource(self)
        self.with_raw_response = TaskadeWithRawResponse(self)
        self.with_streaming_response = TaskadeWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncTaskade(AsyncAPIClient):
    workspaces: workspaces.AsyncWorkspacesResource
    projects: projects.AsyncProjectsResource
    folders: folders.AsyncFoldersResource
    me: me.AsyncMeResource
    agents: agents.AsyncAgentsResource
    medias: medias.AsyncMediasResource
    public_agents: public_agents.AsyncPublicAgentsResource
    with_raw_response: AsyncTaskadeWithRawResponse
    with_streaming_response: AsyncTaskadeWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncTaskade client instance.

        This automatically infers the `api_key` argument from the `TASKADE_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("TASKADE_API_KEY")
        if api_key is None:
            raise TaskadeError(
                "The api_key client option must be set either by passing api_key to the client or by setting the TASKADE_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("TASKADE_BASE_URL")
        if base_url is None:
            base_url = f"https://www.taskade.com/api/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.workspaces = workspaces.AsyncWorkspacesResource(self)
        self.projects = projects.AsyncProjectsResource(self)
        self.folders = folders.AsyncFoldersResource(self)
        self.me = me.AsyncMeResource(self)
        self.agents = agents.AsyncAgentsResource(self)
        self.medias = medias.AsyncMediasResource(self)
        self.public_agents = public_agents.AsyncPublicAgentsResource(self)
        self.with_raw_response = AsyncTaskadeWithRawResponse(self)
        self.with_streaming_response = AsyncTaskadeWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class TaskadeWithRawResponse:
    def __init__(self, client: Taskade) -> None:
        self.workspaces = workspaces.WorkspacesResourceWithRawResponse(client.workspaces)
        self.projects = projects.ProjectsResourceWithRawResponse(client.projects)
        self.folders = folders.FoldersResourceWithRawResponse(client.folders)
        self.me = me.MeResourceWithRawResponse(client.me)
        self.agents = agents.AgentsResourceWithRawResponse(client.agents)
        self.medias = medias.MediasResourceWithRawResponse(client.medias)
        self.public_agents = public_agents.PublicAgentsResourceWithRawResponse(client.public_agents)


class AsyncTaskadeWithRawResponse:
    def __init__(self, client: AsyncTaskade) -> None:
        self.workspaces = workspaces.AsyncWorkspacesResourceWithRawResponse(client.workspaces)
        self.projects = projects.AsyncProjectsResourceWithRawResponse(client.projects)
        self.folders = folders.AsyncFoldersResourceWithRawResponse(client.folders)
        self.me = me.AsyncMeResourceWithRawResponse(client.me)
        self.agents = agents.AsyncAgentsResourceWithRawResponse(client.agents)
        self.medias = medias.AsyncMediasResourceWithRawResponse(client.medias)
        self.public_agents = public_agents.AsyncPublicAgentsResourceWithRawResponse(client.public_agents)


class TaskadeWithStreamedResponse:
    def __init__(self, client: Taskade) -> None:
        self.workspaces = workspaces.WorkspacesResourceWithStreamingResponse(client.workspaces)
        self.projects = projects.ProjectsResourceWithStreamingResponse(client.projects)
        self.folders = folders.FoldersResourceWithStreamingResponse(client.folders)
        self.me = me.MeResourceWithStreamingResponse(client.me)
        self.agents = agents.AgentsResourceWithStreamingResponse(client.agents)
        self.medias = medias.MediasResourceWithStreamingResponse(client.medias)
        self.public_agents = public_agents.PublicAgentsResourceWithStreamingResponse(client.public_agents)


class AsyncTaskadeWithStreamedResponse:
    def __init__(self, client: AsyncTaskade) -> None:
        self.workspaces = workspaces.AsyncWorkspacesResourceWithStreamingResponse(client.workspaces)
        self.projects = projects.AsyncProjectsResourceWithStreamingResponse(client.projects)
        self.folders = folders.AsyncFoldersResourceWithStreamingResponse(client.folders)
        self.me = me.AsyncMeResourceWithStreamingResponse(client.me)
        self.agents = agents.AsyncAgentsResourceWithStreamingResponse(client.agents)
        self.medias = medias.AsyncMediasResourceWithStreamingResponse(client.medias)
        self.public_agents = public_agents.AsyncPublicAgentsResourceWithStreamingResponse(client.public_agents)


Client = Taskade

AsyncClient = AsyncTaskade
