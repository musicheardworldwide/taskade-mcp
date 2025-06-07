# Workspaces

Types:

```python
from taskade.types import (
    Project,
    WorkspaceListResponse,
    WorkspaceCreateProjectResponse,
    WorkspaceListFoldersResponse,
)
```

Methods:

- <code title="get /workspaces">client.workspaces.<a href="./src/taskade/resources/workspaces.py">list</a>() -> <a href="./src/taskade/types/workspace_list_response.py">WorkspaceListResponse</a></code>
- <code title="post /workspaces/{workspaceId}/projects">client.workspaces.<a href="./src/taskade/resources/workspaces.py">create_project</a>(workspace_id, \*\*<a href="src/taskade/types/workspace_create_project_params.py">params</a>) -> <a href="./src/taskade/types/workspace_create_project_response.py">WorkspaceCreateProjectResponse</a></code>
- <code title="get /workspaces/{workspaceId}/folders">client.workspaces.<a href="./src/taskade/resources/workspaces.py">list_folders</a>(workspace_id) -> <a href="./src/taskade/types/workspace_list_folders_response.py">WorkspaceListFoldersResponse</a></code>

# Projects

Types:

```python
from taskade.types import (
    ProjectCreateResponse,
    ProjectRetrieveResponse,
    ProjectCompleteResponse,
    ProjectCopyResponse,
    ProjectCreateFromTemplateResponse,
    ProjectListBlocksResponse,
    ProjectListFieldsResponse,
    ProjectListMembersResponse,
    ProjectRestoreResponse,
)
```

Methods:

- <code title="post /projects">client.projects.<a href="./src/taskade/resources/projects/projects.py">create</a>(\*\*<a href="src/taskade/types/project_create_params.py">params</a>) -> <a href="./src/taskade/types/project_create_response.py">ProjectCreateResponse</a></code>
- <code title="get /projects/{projectId}">client.projects.<a href="./src/taskade/resources/projects/projects.py">retrieve</a>(project_id) -> <a href="./src/taskade/types/project_retrieve_response.py">ProjectRetrieveResponse</a></code>
- <code title="post /projects/{projectId}/complete">client.projects.<a href="./src/taskade/resources/projects/projects.py">complete</a>(project_id) -> <a href="./src/taskade/types/project_complete_response.py">ProjectCompleteResponse</a></code>
- <code title="post /projects/{projectId}/copy">client.projects.<a href="./src/taskade/resources/projects/projects.py">copy</a>(project_id, \*\*<a href="src/taskade/types/project_copy_params.py">params</a>) -> <a href="./src/taskade/types/project_copy_response.py">ProjectCopyResponse</a></code>
- <code title="post /projects/from-template">client.projects.<a href="./src/taskade/resources/projects/projects.py">create_from_template</a>(\*\*<a href="src/taskade/types/project_create_from_template_params.py">params</a>) -> <a href="./src/taskade/types/project_create_from_template_response.py">ProjectCreateFromTemplateResponse</a></code>
- <code title="get /projects/{projectId}/blocks">client.projects.<a href="./src/taskade/resources/projects/projects.py">list_blocks</a>(project_id, \*\*<a href="src/taskade/types/project_list_blocks_params.py">params</a>) -> <a href="./src/taskade/types/project_list_blocks_response.py">ProjectListBlocksResponse</a></code>
- <code title="get /projects/{projectId}/fields">client.projects.<a href="./src/taskade/resources/projects/projects.py">list_fields</a>(project_id) -> <a href="./src/taskade/types/project_list_fields_response.py">ProjectListFieldsResponse</a></code>
- <code title="get /projects/{projectId}/members">client.projects.<a href="./src/taskade/resources/projects/projects.py">list_members</a>(project_id, \*\*<a href="src/taskade/types/project_list_members_params.py">params</a>) -> <a href="./src/taskade/types/project_list_members_response.py">ProjectListMembersResponse</a></code>
- <code title="post /projects/{projectId}/restore">client.projects.<a href="./src/taskade/resources/projects/projects.py">restore</a>(project_id) -> <a href="./src/taskade/types/project_restore_response.py">ProjectRestoreResponse</a></code>

## ShareLink

Types:

```python
from taskade.types.projects import ProjectShare, ShareLinkRetrieveResponse, ShareLinkEnableResponse
```

Methods:

- <code title="get /projects/{projectId}/shareLink">client.projects.share_link.<a href="./src/taskade/resources/projects/share_link.py">retrieve</a>(project_id) -> <a href="./src/taskade/types/projects/share_link_retrieve_response.py">ShareLinkRetrieveResponse</a></code>
- <code title="put /projects/{projectId}/shareLink">client.projects.share_link.<a href="./src/taskade/resources/projects/share_link.py">enable</a>(project_id) -> <a href="./src/taskade/types/projects/share_link_enable_response.py">ShareLinkEnableResponse</a></code>

## Tasks

Types:

```python
from taskade.types.projects import (
    Task,
    TaskCreateResponse,
    TaskRetrieveResponse,
    TaskUpdateResponse,
    TaskListResponse,
    TaskDeleteResponse,
    TaskCompleteResponse,
    TaskMoveResponse,
    TaskUncompleteResponse,
)
```

Methods:

- <code title="post /projects/{projectId}/tasks/">client.projects.tasks.<a href="./src/taskade/resources/projects/tasks/tasks.py">create</a>(project_id, \*\*<a href="src/taskade/types/projects/task_create_params.py">params</a>) -> <a href="./src/taskade/types/projects/task_create_response.py">TaskCreateResponse</a></code>
- <code title="get /projects/{projectId}/tasks/{taskId}">client.projects.tasks.<a href="./src/taskade/resources/projects/tasks/tasks.py">retrieve</a>(task_id, \*, project_id) -> <a href="./src/taskade/types/projects/task_retrieve_response.py">TaskRetrieveResponse</a></code>
- <code title="put /projects/{projectId}/tasks/{taskId}">client.projects.tasks.<a href="./src/taskade/resources/projects/tasks/tasks.py">update</a>(task_id, \*, project_id, \*\*<a href="src/taskade/types/projects/task_update_params.py">params</a>) -> <a href="./src/taskade/types/projects/task_update_response.py">TaskUpdateResponse</a></code>
- <code title="get /projects/{projectId}/tasks">client.projects.tasks.<a href="./src/taskade/resources/projects/tasks/tasks.py">list</a>(project_id, \*\*<a href="src/taskade/types/projects/task_list_params.py">params</a>) -> <a href="./src/taskade/types/projects/task_list_response.py">TaskListResponse</a></code>
- <code title="delete /projects/{projectId}/tasks/{taskId}">client.projects.tasks.<a href="./src/taskade/resources/projects/tasks/tasks.py">delete</a>(task_id, \*, project_id) -> <a href="./src/taskade/types/projects/task_delete_response.py">TaskDeleteResponse</a></code>
- <code title="post /projects/{projectId}/tasks/{taskId}/complete">client.projects.tasks.<a href="./src/taskade/resources/projects/tasks/tasks.py">complete</a>(task_id, \*, project_id) -> <a href="./src/taskade/types/projects/task_complete_response.py">TaskCompleteResponse</a></code>
- <code title="put /projects/{projectId}/tasks/{taskId}/move">client.projects.tasks.<a href="./src/taskade/resources/projects/tasks/tasks.py">move</a>(task_id, \*, project_id, \*\*<a href="src/taskade/types/projects/task_move_params.py">params</a>) -> <a href="./src/taskade/types/projects/task_move_response.py">TaskMoveResponse</a></code>
- <code title="post /projects/{projectId}/tasks/{taskId}/uncomplete">client.projects.tasks.<a href="./src/taskade/resources/projects/tasks/tasks.py">uncomplete</a>(task_id, \*, project_id) -> <a href="./src/taskade/types/projects/task_uncomplete_response.py">TaskUncompleteResponse</a></code>

### Assignees

Types:

```python
from taskade.types.projects.tasks import (
    User,
    AssigneeUpdateResponse,
    AssigneeListResponse,
    AssigneeRemoveResponse,
)
```

Methods:

- <code title="put /projects/{projectId}/tasks/{taskId}/assignees">client.projects.tasks.assignees.<a href="./src/taskade/resources/projects/tasks/assignees.py">update</a>(task_id, \*, project_id, \*\*<a href="src/taskade/types/projects/tasks/assignee_update_params.py">params</a>) -> <a href="./src/taskade/types/projects/tasks/assignee_update_response.py">AssigneeUpdateResponse</a></code>
- <code title="get /projects/{projectId}/tasks/{taskId}/assignees">client.projects.tasks.assignees.<a href="./src/taskade/resources/projects/tasks/assignees.py">list</a>(task_id, \*, project_id) -> <a href="./src/taskade/types/projects/tasks/assignee_list_response.py">AssigneeListResponse</a></code>
- <code title="delete /projects/{projectId}/tasks/{taskId}/assignees/{assigneeHandle}">client.projects.tasks.assignees.<a href="./src/taskade/resources/projects/tasks/assignees.py">remove</a>(assignee_handle, \*, project_id, task_id) -> <a href="./src/taskade/types/projects/tasks/assignee_remove_response.py">AssigneeRemoveResponse</a></code>

### Date

Types:

```python
from taskade.types.projects.tasks import (
    TaskDate,
    DateRetrieveResponse,
    DateUpdateResponse,
    DateDeleteResponse,
)
```

Methods:

- <code title="get /projects/{projectId}/tasks/{taskId}/date">client.projects.tasks.date.<a href="./src/taskade/resources/projects/tasks/date.py">retrieve</a>(task_id, \*, project_id) -> <a href="./src/taskade/types/projects/tasks/date_retrieve_response.py">DateRetrieveResponse</a></code>
- <code title="put /projects/{projectId}/tasks/{taskId}/date">client.projects.tasks.date.<a href="./src/taskade/resources/projects/tasks/date.py">update</a>(task_id, \*, project_id, \*\*<a href="src/taskade/types/projects/tasks/date_update_params.py">params</a>) -> <a href="./src/taskade/types/projects/tasks/date_update_response.py">DateUpdateResponse</a></code>
- <code title="delete /projects/{projectId}/tasks/{taskId}/date">client.projects.tasks.date.<a href="./src/taskade/resources/projects/tasks/date.py">delete</a>(task_id, \*, project_id) -> <a href="./src/taskade/types/projects/tasks/date_delete_response.py">DateDeleteResponse</a></code>

### Note

Types:

```python
from taskade.types.projects.tasks import (
    TaskNote,
    NoteRetrieveResponse,
    NoteUpdateResponse,
    NoteDeleteResponse,
)
```

Methods:

- <code title="get /projects/{projectId}/tasks/{taskId}/note">client.projects.tasks.note.<a href="./src/taskade/resources/projects/tasks/note.py">retrieve</a>(task_id, \*, project_id) -> <a href="./src/taskade/types/projects/tasks/note_retrieve_response.py">NoteRetrieveResponse</a></code>
- <code title="put /projects/{projectId}/tasks/{taskId}/note">client.projects.tasks.note.<a href="./src/taskade/resources/projects/tasks/note.py">update</a>(task_id, \*, project_id, \*\*<a href="src/taskade/types/projects/tasks/note_update_params.py">params</a>) -> <a href="./src/taskade/types/projects/tasks/note_update_response.py">NoteUpdateResponse</a></code>
- <code title="delete /projects/{projectId}/tasks/{taskId}/note">client.projects.tasks.note.<a href="./src/taskade/resources/projects/tasks/note.py">delete</a>(task_id, \*, project_id) -> <a href="./src/taskade/types/projects/tasks/note_delete_response.py">NoteDeleteResponse</a></code>

### Fields

Types:

```python
from taskade.types.projects.tasks import (
    FieldValue,
    FieldRetrieveResponse,
    FieldUpdateResponse,
    FieldListResponse,
    FieldDeleteResponse,
)
```

Methods:

- <code title="get /projects/{projectId}/tasks/{taskId}/fields/{fieldId}">client.projects.tasks.fields.<a href="./src/taskade/resources/projects/tasks/fields.py">retrieve</a>(field_id, \*, project_id, task_id) -> <a href="./src/taskade/types/projects/tasks/field_retrieve_response.py">FieldRetrieveResponse</a></code>
- <code title="put /projects/{projectId}/tasks/{taskId}/fields/{fieldId}">client.projects.tasks.fields.<a href="./src/taskade/resources/projects/tasks/fields.py">update</a>(field_id, \*, project_id, task_id, \*\*<a href="src/taskade/types/projects/tasks/field_update_params.py">params</a>) -> <a href="./src/taskade/types/projects/tasks/field_update_response.py">FieldUpdateResponse</a></code>
- <code title="get /projects/{projectId}/tasks/{taskId}/fields">client.projects.tasks.fields.<a href="./src/taskade/resources/projects/tasks/fields.py">list</a>(task_id, \*, project_id) -> <a href="./src/taskade/types/projects/tasks/field_list_response.py">FieldListResponse</a></code>
- <code title="delete /projects/{projectId}/tasks/{taskId}/fields/{fieldId}">client.projects.tasks.fields.<a href="./src/taskade/resources/projects/tasks/fields.py">delete</a>(field_id, \*, project_id, task_id) -> <a href="./src/taskade/types/projects/tasks/field_delete_response.py">FieldDeleteResponse</a></code>

# Folders

Types:

```python
from taskade.types import (
    SpaceAgent,
    FolderGenerateAgentResponse,
    FolderListMediasResponse,
    FolderListProjectTemplatesResponse,
    FolderListProjectsResponse,
)
```

Methods:

- <code title="post /folders/{folderId}/agent-generate">client.folders.<a href="./src/taskade/resources/folders/folders.py">generate_agent</a>(folder_id, \*\*<a href="src/taskade/types/folder_generate_agent_params.py">params</a>) -> <a href="./src/taskade/types/folder_generate_agent_response.py">FolderGenerateAgentResponse</a></code>
- <code title="get /folders/{folderId}/medias">client.folders.<a href="./src/taskade/resources/folders/folders.py">list_medias</a>(folder_id, \*\*<a href="src/taskade/types/folder_list_medias_params.py">params</a>) -> <a href="./src/taskade/types/folder_list_medias_response.py">FolderListMediasResponse</a></code>
- <code title="get /folders/{folderId}/project-templates">client.folders.<a href="./src/taskade/resources/folders/folders.py">list_project_templates</a>(folder_id, \*\*<a href="src/taskade/types/folder_list_project_templates_params.py">params</a>) -> <a href="./src/taskade/types/folder_list_project_templates_response.py">FolderListProjectTemplatesResponse</a></code>
- <code title="get /folders/{folderId}/projects">client.folders.<a href="./src/taskade/resources/folders/folders.py">list_projects</a>(folder_id) -> <a href="./src/taskade/types/folder_list_projects_response.py">FolderListProjectsResponse</a></code>

## Agents

Types:

```python
from taskade.types.folders import AgentCreateResponse, AgentListResponse
```

Methods:

- <code title="post /folders/{folderId}/agents">client.folders.agents.<a href="./src/taskade/resources/folders/agents.py">create</a>(folder_id, \*\*<a href="src/taskade/types/folders/agent_create_params.py">params</a>) -> <a href="./src/taskade/types/folders/agent_create_response.py">AgentCreateResponse</a></code>
- <code title="get /folders/{folderId}/agents">client.folders.agents.<a href="./src/taskade/resources/folders/agents.py">list</a>(folder_id, \*\*<a href="src/taskade/types/folders/agent_list_params.py">params</a>) -> <a href="./src/taskade/types/folders/agent_list_response.py">AgentListResponse</a></code>

# Me

Types:

```python
from taskade.types import MeListProjectsResponse
```

Methods:

- <code title="get /me/projects">client.me.<a href="./src/taskade/resources/me.py">list_projects</a>(\*\*<a href="src/taskade/types/me_list_projects_params.py">params</a>) -> <a href="./src/taskade/types/me_list_projects_response.py">MeListProjectsResponse</a></code>

# Agents

Types:

```python
from taskade.types import (
    AgentRetrieveResponse,
    AgentUpdateResponse,
    AgentDeleteResponse,
    AgentEnablePublicAccessResponse,
)
```

Methods:

- <code title="get /agents/{agentId}">client.agents.<a href="./src/taskade/resources/agents/agents.py">retrieve</a>(agent_id) -> <a href="./src/taskade/types/agent_retrieve_response.py">AgentRetrieveResponse</a></code>
- <code title="patch /agents/{agentId}">client.agents.<a href="./src/taskade/resources/agents/agents.py">update</a>(agent_id, \*\*<a href="src/taskade/types/agent_update_params.py">params</a>) -> <a href="./src/taskade/types/agent_update_response.py">AgentUpdateResponse</a></code>
- <code title="delete /agents/{agentId}">client.agents.<a href="./src/taskade/resources/agents/agents.py">delete</a>(agent_id) -> <a href="./src/taskade/types/agent_delete_response.py">AgentDeleteResponse</a></code>
- <code title="put /agents/{agentId}/publicAccess">client.agents.<a href="./src/taskade/resources/agents/agents.py">enable_public_access</a>(agent_id) -> <a href="./src/taskade/types/agent_enable_public_access_response.py">AgentEnablePublicAccessResponse</a></code>

## PublicAgent

Types:

```python
from taskade.types.agents import PublicAgentRetrieveResponse, PublicAgentUpdateResponse
```

Methods:

- <code title="get /agents/{agentId}/public-agent">client.agents.public_agent.<a href="./src/taskade/resources/agents/public_agent.py">retrieve</a>(agent_id) -> <a href="./src/taskade/types/agents/public_agent_retrieve_response.py">PublicAgentRetrieveResponse</a></code>
- <code title="patch /agents/{agentId}/public-agent">client.agents.public_agent.<a href="./src/taskade/resources/agents/public_agent.py">update</a>(agent_id, \*\*<a href="src/taskade/types/agents/public_agent_update_params.py">params</a>) -> <a href="./src/taskade/types/agents/public_agent_update_response.py">PublicAgentUpdateResponse</a></code>

## Knowledge

### Project

Types:

```python
from taskade.types.agents.knowledge import ProjectCreateResponse, ProjectDeleteResponse
```

Methods:

- <code title="post /agents/{agentId}/knowledge/project">client.agents.knowledge.project.<a href="./src/taskade/resources/agents/knowledge/project.py">create</a>(agent_id, \*\*<a href="src/taskade/types/agents/knowledge/project_create_params.py">params</a>) -> <a href="./src/taskade/types/agents/knowledge/project_create_response.py">ProjectCreateResponse</a></code>
- <code title="delete /agents/{agentId}/knowledge/project/{projectId}">client.agents.knowledge.project.<a href="./src/taskade/resources/agents/knowledge/project.py">delete</a>(project_id, \*, agent_id) -> <a href="./src/taskade/types/agents/knowledge/project_delete_response.py">ProjectDeleteResponse</a></code>

### Media

Types:

```python
from taskade.types.agents.knowledge import MediaCreateResponse, MediaDeleteResponse
```

Methods:

- <code title="post /agents/{agentId}/knowledge/media">client.agents.knowledge.media.<a href="./src/taskade/resources/agents/knowledge/media.py">create</a>(agent_id, \*\*<a href="src/taskade/types/agents/knowledge/media_create_params.py">params</a>) -> <a href="./src/taskade/types/agents/knowledge/media_create_response.py">MediaCreateResponse</a></code>
- <code title="delete /agents/{agentId}/knowledge/media/{mediaId}">client.agents.knowledge.media.<a href="./src/taskade/resources/agents/knowledge/media.py">delete</a>(media_id, \*, agent_id) -> <a href="./src/taskade/types/agents/knowledge/media_delete_response.py">MediaDeleteResponse</a></code>

## Convos

Types:

```python
from taskade.types.agents import Convo, ConvoRetrieveResponse, ConvoListResponse
```

Methods:

- <code title="get /agents/{agentId}/convos/{convoId}">client.agents.convos.<a href="./src/taskade/resources/agents/convos.py">retrieve</a>(convo_id, \*, agent_id) -> <a href="./src/taskade/types/agents/convo_retrieve_response.py">ConvoRetrieveResponse</a></code>
- <code title="get /agents/{agentId}/convos/">client.agents.convos.<a href="./src/taskade/resources/agents/convos.py">list</a>(agent_id, \*\*<a href="src/taskade/types/agents/convo_list_params.py">params</a>) -> <a href="./src/taskade/types/agents/convo_list_response.py">ConvoListResponse</a></code>

# Medias

Types:

```python
from taskade.types import Media, MediaRetrieveResponse, MediaDeleteResponse
```

Methods:

- <code title="get /medias/{mediaId}">client.medias.<a href="./src/taskade/resources/medias.py">retrieve</a>(media_id) -> <a href="./src/taskade/types/media_retrieve_response.py">MediaRetrieveResponse</a></code>
- <code title="delete /medias/{mediaId}">client.medias.<a href="./src/taskade/resources/medias.py">delete</a>(media_id) -> <a href="./src/taskade/types/media_delete_response.py">MediaDeleteResponse</a></code>

# PublicAgents

Types:

```python
from taskade.types import PublicAgentRetrieveResponse
```

Methods:

- <code title="get /public-agents/{publicAgentId}">client.public_agents.<a href="./src/taskade/resources/public_agents.py">retrieve</a>(public_agent_id) -> <a href="./src/taskade/types/public_agent_retrieve_response.py">PublicAgentRetrieveResponse</a></code>
