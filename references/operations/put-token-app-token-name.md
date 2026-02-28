# PUT /token/{app}/{token_name}

**Resource:** [Access token](../resources/Access-token.md)
**Refresh a access token for a user**
**Operation ID:** `put--token-{app}-{token_name}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `app` | path | enum: git, starship | Yes | application |
| `token_name` | path | string | Yes | token_name |
| `current_user` | query | string | Yes | current user, the owner |
| `expired_at` | query | string | No | new expire time, in format RFC3339, like 2006-01-02T15:04:05Z07:00 |

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
