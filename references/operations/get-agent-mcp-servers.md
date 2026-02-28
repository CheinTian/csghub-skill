# GET /agent/mcp-servers

**Resource:** [Agent](../resources/Agent.md)
**List agent MCP servers**
**Operation ID:** `get--agent-mcp-servers`

Get all agent MCP servers (built-in and user-created) with filtering and pagination

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `search` | query | string | No | Search term for name field |
| `built_in` | query | boolean | No | Filter by built-in status |
| `protocol` | query | enum: streamable, sse | No | Filter by protocol |
| `need_install` | query | boolean | No | Filter by need_install status |
| `status` | query | enum: connected, error | No | Filter by status |
| `installed` | query | boolean | No | Filter by installed status |
| `per` | query | integer | No | Items per page |
| `page` | query | integer | No | Page number |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 401 | Unauthorized |
| 500 | Internal server error |

## Security

- **ApiKey**
