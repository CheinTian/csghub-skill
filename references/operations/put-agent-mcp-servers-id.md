# PUT /agent/mcp-servers/{id}

**Resource:** [Agent](../resources/Agent.md)
**Update an existing agent MCP server**
**Operation ID:** `put--agent-mcp-servers-{id}`

Update the details of an existing agent MCP server (built-in or user-created). For built-in servers, updates are stored as user overrides. For user-created servers, the record is directly updated.

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | Server ID (format: builtin:{id} or user:{id}) |

## Request Body

Updated MCP server data

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UpdateAgentMCPServerRequest](../schemas/types-UpdateAgentMCPServerRequest/types-UpdateAgentMCPServerRequest.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

**Success Response Schema:**

[types.Response](../schemas/types-Response/types-Response.md)

## Security

- **ApiKey**
