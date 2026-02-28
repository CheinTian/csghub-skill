# Agent

## Operations

| Method | Path | Summary | Details |
|--------|------|---------|----------|
| GET | `/admin/agent/configs` | List Agent Configs | [View](../operations/get-admin-agent-configs.md) |
| POST | `/admin/agent/configs` | Create Agent Config | [View](../operations/post-admin-agent-configs.md) |
| GET | `/admin/agent/configs/:id` | Get Agent Config | [View](../operations/get-admin-agent-configs-id.md) |
| PUT | `/admin/agent/configs/:id` | Update Agent Config | [View](../operations/put-admin-agent-configs-id.md) |
| DELETE | `/admin/agent/configs/:id` | Delete Agent Config | [View](../operations/delete-admin-agent-configs-id.md) |
| GET | `/agent/instances` | List agent instances for the current user | [View](../operations/get-agent-instances.md) |
| POST | `/agent/instances` | Create a new agent instance | [View](../operations/post-agent-instances.md) |
| PUT | `/agent/instances/by-content-id/{type}/{content_id}` | Update an existing agent instance by type and content id | [View](../operations/put-agent-instances-by-content-id-type-content-id.md) |
| DELETE | `/agent/instances/by-content-id/{type}/{content_id}` | Delete an agent instance by type and content id | [View](../operations/delete-agent-instances-by-content-id-type-content-id.md) |
| POST | `/agent/instances/monitor` | Monitor status for agent instances | [View](../operations/post-agent-instances-monitor.md) |
| GET | `/agent/instances/status` | Get status for multiple agent instances with SSE | [View](../operations/get-agent-instances-status.md) |
| GET | `/agent/instances/{id}` | Get an agent instance by ID | [View](../operations/get-agent-instances-id.md) |
| PUT | `/agent/instances/{id}` | Update an existing agent instance | [View](../operations/put-agent-instances-id.md) |
| DELETE | `/agent/instances/{id}` | Delete an agent instance | [View](../operations/delete-agent-instances-id.md) |
| GET | `/agent/instances/{id}/sessions` | List sessions by instance ID | [View](../operations/get-agent-instances-id-sessions.md) |
| POST | `/agent/instances/{id}/sessions` | Create a new session for an agent instance | [View](../operations/post-agent-instances-id-sessions.md) |
| GET | `/agent/instances/{id}/sessions/{session_uuid}` | Get session by session UUID | [View](../operations/get-agent-instances-id-sessions-session-uuid.md) |
| PUT | `/agent/instances/{id}/sessions/{session_uuid}` | Update session by session UUID | [View](../operations/put-agent-instances-id-sessions-session-uuid.md) |
| DELETE | `/agent/instances/{id}/sessions/{session_uuid}` | Delete session by session UUID | [View](../operations/delete-agent-instances-id-sessions-session-uuid.md) |
| GET | `/agent/instances/{id}/sessions/{session_uuid}/histories` | List session histories by session UUID | [View](../operations/get-agent-instances-id-sessions-session-uuid-histories.md) |
| POST | `/agent/instances/{id}/sessions/{session_uuid}/histories` | Create session histories for an agent instance session | [View](../operations/post-agent-instances-id-sessions-session-uuid-histories.md) |
| PUT | `/agent/instances/{id}/sessions/{session_uuid}/histories/{msg_uuid}/feedback` | Update the feedback of a session history message | [View](../operations/put-agent-instances-id-sessions-session-uuid-histories-msg-uuid-feedback.md) |
| PUT | `/agent/instances/{id}/sessions/{session_uuid}/histories/{msg_uuid}/rewrite` | Rewrite an output message | [View](../operations/put-agent-instances-id-sessions-session-uuid-histories-msg-uuid-rewrite.md) |
| POST | `/agent/instances/{id}/sessions/{session_uuid}/share` | Share a session | [View](../operations/post-agent-instances-id-sessions-session-uuid-share.md) |
| GET | `/agent/knowledge-bases` | List agent knowledge bases | [View](../operations/get-agent-knowledge-bases.md) |
| POST | `/agent/knowledge-bases` | Create a new agent knowledge base | [View](../operations/post-agent-knowledge-bases.md) |
| PUT | `/agent/knowledge-bases/content-id/{content_id}` | Update an agent knowledge base by ContentID | [View](../operations/put-agent-knowledge-bases-content-id-content-id.md) |
| DELETE | `/agent/knowledge-bases/content-id/{content_id}` | Delete an agent knowledge base by ContentID | [View](../operations/delete-agent-knowledge-bases-content-id-content-id.md) |
| GET | `/agent/knowledge-bases/{id}` | Get an agent knowledge base by ID | [View](../operations/get-agent-knowledge-bases-id.md) |
| PUT | `/agent/knowledge-bases/{id}` | Update an existing agent knowledge base | [View](../operations/put-agent-knowledge-bases-id.md) |
| DELETE | `/agent/knowledge-bases/{id}` | Delete an agent knowledge base | [View](../operations/delete-agent-knowledge-bases-id.md) |
| GET | `/agent/mcp-servers` | List agent MCP servers | [View](../operations/get-agent-mcp-servers.md) |
| POST | `/agent/mcp-servers` | Create a new agent MCP server | [View](../operations/post-agent-mcp-servers.md) |
| POST | `/agent/mcp-servers/inspect` | Inspect an MCP server and fetch capabilities | [View](../operations/post-agent-mcp-servers-inspect.md) |
| POST | `/agent/mcp-servers/monitor` | Monitor status for MCP servers | [View](../operations/post-agent-mcp-servers-monitor.md) |
| GET | `/agent/mcp-servers/status` | Get status for MCP servers with SSE | [View](../operations/get-agent-mcp-servers-status.md) |
| GET | `/agent/mcp-servers/{id}` | Get an agent MCP server by ID | [View](../operations/get-agent-mcp-servers-id.md) |
| PUT | `/agent/mcp-servers/{id}` | Update an existing agent MCP server | [View](../operations/put-agent-mcp-servers-id.md) |
| DELETE | `/agent/mcp-servers/{id}` | Delete an agent MCP server or config | [View](../operations/delete-agent-mcp-servers-id.md) |
| GET | `/agent/prompts` | List agent prompts | [View](../operations/get-agent-prompts.md) |
| POST | `/agent/prompts/optimize` | Optimize agent prompt | [View](../operations/post-agent-prompts-optimize.md) |
| GET | `/agent/shared/session` | Get shared session by share uuid | [View](../operations/get-agent-shared-session.md) |
| GET | `/agent/tasks` | List agent tasks | [View](../operations/get-agent-tasks.md) |
| GET | `/agent/tasks/{id}` | Get agent task detail | [View](../operations/get-agent-tasks-id.md) |
| GET | `/agent/templates` | List agent templates for the current user | [View](../operations/get-agent-templates.md) |
| POST | `/agent/templates` | Create a new agent template | [View](../operations/post-agent-templates.md) |
| GET | `/agent/templates/{id}` | Get an agent template by ID | [View](../operations/get-agent-templates-id.md) |
| PUT | `/agent/templates/{id}` | Update an existing agent template | [View](../operations/put-agent-templates-id.md) |
| DELETE | `/agent/templates/{id}` | Delete an agent template | [View](../operations/delete-agent-templates-id.md) |
| GET | `/agent/templates/{id}/instances` | List agent instances by template ID | [View](../operations/get-agent-templates-id-instances.md) |
| POST | `/agent/user-preferences` | Set a preference for an entity (e.g., pin) | [View](../operations/post-agent-user-preferences.md) |
| DELETE | `/agent/user-preferences` | Remove a preference for an entity (e.g., unpin) | [View](../operations/delete-agent-user-preferences.md) |
