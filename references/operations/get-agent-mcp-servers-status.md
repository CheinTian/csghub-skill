# GET /agent/mcp-servers/status

**Resource:** [Agent](../resources/Agent.md)
**Get status for MCP servers with SSE**
**Operation ID:** `get--agent-mcp-servers-status`

Monitor status of MCP servers using Server-Sent Events. Each event contains status update for a single MCP server.

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `monitor_id` | query | string | Yes | Monitor UUID |

## Responses

| Status | Description |
|--------|-------------|
| 200 | SSE stream with status updates |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
