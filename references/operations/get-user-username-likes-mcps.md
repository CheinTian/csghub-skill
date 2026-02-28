# GET /user/{username}/likes/mcps

**Resource:** [User](../resources/User.md)
**Get user likes mcp servers**
**Operation ID:** `get--user-{username}-likes-mcps`

get user likes mcp servers

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
