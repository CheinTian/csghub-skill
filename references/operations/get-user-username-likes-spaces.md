# GET /user/{username}/likes/spaces

**Resource:** [User](../resources/User.md)
**Get user likes spaces**
**Operation ID:** `get--user-{username}-likes-spaces`

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
