# POST /organization/{namespace}/members

**Resource:** [Member](../resources/Member.md)
**Create new membership between org and user**
**Operation ID:** `post--organization-{namespace}-members`

user will be added to org with a role

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | org name |
| `current_user` | query | string | No | the op user |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [handler.Create.addMemberRequest](../schemas/handler-Create-addMemberRequest/handler-Create-addMemberRequest.md)

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
