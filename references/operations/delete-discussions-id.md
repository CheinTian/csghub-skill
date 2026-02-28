# DELETE /discussions/{id}

**Resource:** [Discussion](../resources/Discussion.md)
**Delete a discussion**
**Operation ID:** `delete--discussions-{id}`

delete a discussion

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | the discussion id |
| `current_user` | query | string | Yes | current user, the owner of the discussion |

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
