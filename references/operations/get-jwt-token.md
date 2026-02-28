# GET /jwt/{token}

**Resource:** [JWT](../resources/JWT.md)
**verify jwt token and return user info**
**Operation ID:** `get--jwt-{token}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `token` | path | string | Yes | token |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

**Success Response Schema:**

[types.User](../schemas/types-User/types-User.md)

## Security

- **ApiKey**
