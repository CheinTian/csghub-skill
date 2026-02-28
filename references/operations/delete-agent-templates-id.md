# DELETE /agent/templates/{id}

**Resource:** [Agent](../resources/Agent.md)
**Delete an agent template**
**Operation ID:** `delete--agent-templates-{id}`

Permanently delete an agent template

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer (int64) | Yes | Template ID |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 403 | Forbidden |
| 500 | Internal server error |

**Success Response Schema:**

[types.Response](../schemas/types-Response/types-Response.md)

## Security

- **ApiKey**
