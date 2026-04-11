# DELETE /admin/gateway/mcp-servers/{id}

**Resource:** [MCP Servers](../resources/MCP-Servers.md)
**[Admin] Delete an MCP server**
**Operation ID:** `delete--admin-gateway-mcp-servers-{id}`

Delete a gateway MCP server by ID

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | MCP server ID |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
