# DELETE /organization/{namespace}/members/{username}

**Resource:** [Member](../resources/Member.md)
**Remove membership between org and user**
**Operation ID:** `delete--organization-{namespace}-members-{username}`

user's role will be remove from org

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | org name |
| `username` | path | string | Yes | user name |
| `current_user` | query | string | No | the op user |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.RemoveMemberRequest](../schemas/types-RemoveMemberRequest/types-RemoveMemberRequest.md)

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
