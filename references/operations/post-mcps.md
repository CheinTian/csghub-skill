# POST /mcps

**Resource:** [MCP](../resources/MCP.md)
**Create a new mcp server**
**Operation ID:** `post--mcps`

create a new mcp server

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `current_user` | query | string | No | current user, the owner |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreateMCPServerReq](../schemas/types-CreateMCPServerReq/types-CreateMCPServerReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
