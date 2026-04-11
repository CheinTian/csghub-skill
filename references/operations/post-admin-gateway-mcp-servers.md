# POST /admin/gateway/mcp-servers

**Resource:** [MCP Servers](../resources/MCP-Servers.md)
**[Admin] Create an MCP server**
**Operation ID:** `post--admin-gateway-mcp-servers`

Create a new gateway MCP server

## Request Body

MCP server request

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreateGatewayMCPServerReq](../schemas/types-CreateGatewayMCPServerReq/types-CreateGatewayMCPServerReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
