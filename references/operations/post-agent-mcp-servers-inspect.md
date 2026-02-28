# POST /agent/mcp-servers/inspect

**Resource:** [Agent](../resources/Agent.md)
**Inspect an MCP server and fetch capabilities**
**Operation ID:** `post--agent-mcp-servers-inspect`

Inspect an MCP server and fetch its capabilities (tools, resources, prompts, resource templates). Returns the connection status and capabilities.

## Request Body

Inspect MCP server request

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.InspectMCPServerRequest](../schemas/types-InspectMCPServerRequest/types-InspectMCPServerRequest.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
