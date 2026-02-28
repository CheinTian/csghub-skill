# POST /agent/mcp-servers/monitor

**Resource:** [Agent](../resources/Agent.md)
**Monitor status for MCP servers**
**Operation ID:** `post--agent-mcp-servers-monitor`

## Request Body

MCP server monitor request

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.AgentMCPServerMonitorRequest](../schemas/types-AgentMCPServerMonitorRequest/types-AgentMCPServerMonitorRequest.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
