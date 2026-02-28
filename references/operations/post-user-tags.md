# POST /user/tags

**Resource:** [User](../resources/User.md)
**ResetUserTags**
**Operation ID:** `post--user-tags`

Allows a user to reset their own tags. This endpoint is only for users to manage their personal tags, not for administrators to set tags for other users.

## Request Body

tagIDs

**Required:** Yes

**Content Types:** `application/json`

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
