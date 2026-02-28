# PUT /user/{id}

**Resource:** [User](../resources/User.md)
**Update user. If change user name, should only send 'new_username' in the request body.**
**Operation ID:** `put--user-{id}`

update user

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | user identifier, could be username(depricated) or uuid |
| `current_user` | query | string | Yes | current user |
| `type` | query | enum: uuid, username | No | type of identifier, uuid or username, default is username |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UpdateUserRequest](../schemas/types-UpdateUserRequest/types-UpdateUserRequest.md)

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
