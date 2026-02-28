# DELETE /space_resources/{id}

**Resource:** [SpaceReource](../resources/SpaceReource.md)
**Delete a exist space resource**
**Operation ID:** `delete--space_resources-{id}`

delete a exist space resource

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | id |

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
