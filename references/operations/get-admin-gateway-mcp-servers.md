# GET /admin/gateway/mcp-servers

**Resource:** [MCP Servers](../resources/MCP-Servers.md)
**[Admin] List MCP servers**
**Operation ID:** `get--admin-gateway-mcp-servers`

List all gateway MCP servers (admin only)

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `search` | query | string | No | search by name/description |
| `status` | query | enum: connected, error | No | status |
| `exact_match` | query | boolean | No | exact match (disables fuzzy search) |
| `per` | query | integer | No | per page |
| `page` | query | integer | No | page |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
