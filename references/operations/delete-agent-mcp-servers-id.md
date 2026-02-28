# DELETE /agent/mcp-servers/{id}

**Resource:** [Agent](../resources/Agent.md)
**Delete an agent MCP server or config**
**Operation ID:** `delete--agent-mcp-servers-{id}`

For built-in servers: delete user's override config. For user-created servers: permanently delete the server.

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | Server ID (format: builtin:{id} or user:{id}) |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 403 | Forbidden |
| 500 | Internal server error |

**Success Response Schema:**

[types.Response](../schemas/types-Response/types-Response.md)

## Security

- **ApiKey**
