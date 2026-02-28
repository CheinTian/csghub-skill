# GET /user/{username}/likes/codes

**Resource:** [User](../resources/User.md)
**Get user likes codes**
**Operation ID:** `get--user-{username}-likes-codes`

get user likes codes

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `username` | path | string | Yes | username |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
