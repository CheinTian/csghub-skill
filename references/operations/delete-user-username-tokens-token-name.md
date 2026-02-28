# DELETE /user/{username}/tokens/{token_name}

**Resource:** [Access token](../resources/Access-token.md)
**[Deprecated: use DELETE:/token/{app}/{token_name} instead]**
**Operation ID:** `delete--user-{username}-tokens-{token_name}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `username` | path | string | Yes | username |
| `token_name` | path | string | Yes | token_name |
| `current_user` | query | string | Yes | current user, the owner |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.DeleteUserTokenRequest](../schemas/types-DeleteUserTokenRequest/types-DeleteUserTokenRequest.md)

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
