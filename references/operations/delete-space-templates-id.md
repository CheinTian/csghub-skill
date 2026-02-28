# DELETE /space_templates/{id}

**Resource:** [SpaceTemplate](../resources/SpaceTemplate.md)
**Delete a exist space template**
**Operation ID:** `delete--space_templates-{id}`

delete a exist space template

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
