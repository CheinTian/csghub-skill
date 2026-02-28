# GET /token/{token_value}

**Resource:** [Access token](../resources/Access-token.md)
**Get token and owner's detail by the token value**
**Operation ID:** `get--token-{token_value}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `token_value` | path | string | Yes | token_value |
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
