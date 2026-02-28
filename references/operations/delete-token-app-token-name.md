# DELETE /token/{app}/{token_name}

**Resource:** [Access token](../resources/Access-token.md)
**Delete access token of a app**
**Operation ID:** `delete--token-{app}-{token_name}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `app` | path | enum: git, starship | Yes | application |
| `token_name` | path | string | Yes | token_name |
| `current_user` | query | string | Yes | current user, the owner |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

**Success Response Schema:**

[types.Response](../schemas/types-Response/types-Response.md)

## Security

- **ApiKey**
