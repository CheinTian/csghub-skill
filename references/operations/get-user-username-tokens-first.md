# GET /user/{username}/tokens/first

**Resource:** [Access token](../resources/Access-token.md)
**Get or create first available access token for a user**
**Operation ID:** `get--user-{username}-tokens-first`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `username` | path | string | Yes | username |
| `current_user` | query | string | No | current user name |
| `app` | query | enum: git, starship | No | application |
| `token_name` | query | string | No | token name |

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
