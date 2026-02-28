# POST /token/{app}/{token_name}

**Resource:** [Access token](../resources/Access-token.md)
**Create access token for an special application**
**Operation ID:** `post--token-{app}-{token_name}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `token_name` | path | string | Yes | token name |
| `app` | path | enum: git, starship | Yes | application |
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
