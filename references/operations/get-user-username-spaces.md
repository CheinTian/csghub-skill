# GET /user/{username}/spaces

**Resource:** [User](../resources/User.md)
**Get user spaces**
**Operation ID:** `get--user-{username}-spaces`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `sdk` | query | string | No | filter by space sdk |
| `username` | path | string | Yes | username |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
