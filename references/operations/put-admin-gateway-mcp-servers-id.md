# PUT /admin/gateway/mcp-servers/{id}

**Resource:** [MCP Servers](../resources/MCP-Servers.md)
**[Admin] Update an MCP server**
**Operation ID:** `put--admin-gateway-mcp-servers-{id}`

Update a gateway MCP server by ID

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | MCP server ID |

## Request Body

Update payload

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.GatewayMCPServerReq](../schemas/types-GatewayMCPServerReq/types-GatewayMCPServerReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 404 | Not found |
| 500 | Internal server error |

## Security

- **ApiKey**
