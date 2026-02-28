# DELETE /tags/{id}

**Resource:** [Tag](../resources/Tag.md)
**Delete a tag by id**
**Operation ID:** `delete--tags-{id}`

Delete a tag by id, used for admin

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | id of the tag |

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
