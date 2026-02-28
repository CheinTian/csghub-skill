# GET /user/{username}/collections

**Resource:** [User](../resources/User.md)
**Get user's collections**
**Operation ID:** `get--user-{username}-collections`

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
