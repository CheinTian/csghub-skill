# DELETE /comments/{id}

**Resource:** [Discussion](../resources/Discussion.md)
**Delete a comment by id**
**Operation ID:** `delete--comments-{id}`

delete a comment by id

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | the comment id |
| `current_user` | query | string | Yes | current user, the owner of the comment |

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
