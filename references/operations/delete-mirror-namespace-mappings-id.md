# DELETE /mirror_namespace_mappings/{id}

**Resource:** [Mirror](../resources/Mirror.md)
**Delete mirror namespace mapping, used for admin**
**Operation ID:** `delete--mirror_namespace_mappings-{id}`

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
