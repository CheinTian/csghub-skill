# DELETE /mirror/sources/{id}

**Resource:** [Mirror](../resources/Mirror.md)
**Delete mirror source, used for admin**
**Operation ID:** `delete--mirror-sources-{id}`

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

- **ApiKey**
