# POST /user/{username}/tokens

**Resource:** [Access token](../resources/Access-token.md)
**[Deprecated: use POST:/token/{app}/{username} instead]**
**Operation ID:** `post--user-{username}-tokens`

create access token for a user

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `username` | path | string | Yes | username |
| `current_user` | query | string | Yes | current user, the owner |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreateUserTokenRequest](../schemas/types-CreateUserTokenRequest/types-CreateUserTokenRequest.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
