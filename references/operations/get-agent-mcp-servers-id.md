# GET /agent/mcp-servers/{id}

**Resource:** [Agent](../resources/Agent.md)
**Get an agent MCP server by ID**
**Operation ID:** `get--agent-mcp-servers-{id}`

Get details of a specific agent MCP server (built-in or user-created)

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | Server ID (format: builtin:{id} or user:{id}) |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
