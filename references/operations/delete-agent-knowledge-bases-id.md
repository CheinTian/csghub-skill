# DELETE /agent/knowledge-bases/{id}

**Resource:** [Agent](../resources/Agent.md)
**Delete an agent knowledge base**
**Operation ID:** `delete--agent-knowledge-bases-{id}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer (int64) | Yes | Knowledge base ID |

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
