# DELETE /user/{username}/close_account

**Resource:** [User](../resources/User.md)
**Delete user**
**Operation ID:** `delete--user-{username}-close_account`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `username` | path | string | Yes | username |
| `current_user` | query | string | Yes | current user |
| `repository` | query | boolean | No | repository |
| `discussion` | query | boolean | No | discussion |

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
