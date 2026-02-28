# PUT /comments/{id}

**Resource:** [Discussion](../resources/Discussion.md)
**Update a comment content by id**
**Operation ID:** `put--comments-{id}`

update a comment content by id

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | the comment id |
| `current_user` | query | string | Yes | current user, the owner of the comment |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UpdateCommentRequest](../schemas/types-UpdateCommentRequest/types-UpdateCommentRequest.md)

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
