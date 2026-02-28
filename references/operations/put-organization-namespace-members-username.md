# PUT /organization/{namespace}/members/{username}

**Resource:** [Member](../resources/Member.md)
**update user membership**
**Operation ID:** `put--organization-{namespace}-members-{username}`

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

**Schema:** [handler.Update.updateMemberRequest](../schemas/handler-Update-updateMemberRequest/handler-Update-updateMemberRequest.md)

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
