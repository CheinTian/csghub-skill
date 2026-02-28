# POST /mcps/{namespace}/{name}/deploy

**Resource:** [MCP](../resources/MCP.md)
**Deploy a exists mcp server as space**
**Operation ID:** `post--mcps-{namespace}-{name}-deploy`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `current_user` | query | string | No | current user |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.DeployMCPServerReq](../schemas/types-DeployMCPServerReq/types-DeployMCPServerReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
