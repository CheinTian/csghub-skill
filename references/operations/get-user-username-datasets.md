# GET /user/{username}/datasets

**Resource:** [User](../resources/User.md)
**Get user datasets**
**Operation ID:** `get--user-{username}-datasets`

get user datasets

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
