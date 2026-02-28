# PUT /mcps/{namespace}/{name}

**Resource:** [MCP](../resources/MCP.md)
**Update a exists mcp server**
**Operation ID:** `put--mcps-{namespace}-{name}`

update a exists mcp server

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `current_user` | query | string | No | current user, the owner |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UpdateMCPServerReq](../schemas/types-UpdateMCPServerReq/types-UpdateMCPServerReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
