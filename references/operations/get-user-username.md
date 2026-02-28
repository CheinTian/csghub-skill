# GET /user/{username}

**Resource:** [User](../resources/User.md)
**Get user info. Admin and the user self can see full info, other users can only see basic info.**
**Operation ID:** `get--user-{username}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `username` | path | string | Yes | username or uuid, defined by the query string 'type' |
| `current_user` | query | string | No | current user |
| `type` | query | enum: username, uuid | No | path param is usernam or uuid, default to username |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
