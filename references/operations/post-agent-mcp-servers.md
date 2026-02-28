# POST /agent/mcp-servers

**Resource:** [Agent](../resources/Agent.md)
**Create a new agent MCP server**
**Operation ID:** `post--agent-mcp-servers`

Create a new agent MCP server configuration

## Request Body

MCP server data

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreateAgentMCPServerRequest](../schemas/types-CreateAgentMCPServerRequest/types-CreateAgentMCPServerRequest.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
