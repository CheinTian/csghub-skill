# GET /admin/gateway/mcp-servers/{id}

**Resource:** [MCP Servers](../resources/MCP-Servers.md)
**[Admin] Get an MCP server by ID**
**Operation ID:** `get--admin-gateway-mcp-servers-{id}`

Get a gateway MCP server by ID (admin only)

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | MCP server ID |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 404 | Not found |
| 500 | Internal server error |

## Security

- **ApiKey**
