# DELETE /collections/{id}

**Resource:** [Collection](../resources/Collection.md)
**Delete a exists collection**
**Operation ID:** `delete--collections-{id}`

delete a exists collection

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | id |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

**Success Response Schema:**

[types.Response](../schemas/types-Response/types-Response.md)

## Security

- **JWT token**
