# GET /user/{username}/tokens

**Resource:** [Access token](../resources/Access-token.md)
**Get all access tokens for a user**
**Operation ID:** `get--user-{username}-tokens`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `username` | path | string | Yes | username |
| `current_user` | query | string | No | current user name |
| `app` | query | enum: git, starship | No | application |

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
