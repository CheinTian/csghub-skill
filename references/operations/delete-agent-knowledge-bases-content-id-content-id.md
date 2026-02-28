# DELETE /agent/knowledge-bases/content-id/{content_id}

**Resource:** [Agent](../resources/Agent.md)
**Delete an agent knowledge base by ContentID**
**Operation ID:** `delete--agent-knowledge-bases-content-id-{content_id}`

Delete an agent knowledge base by its content ID

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `content_id` | path | string | Yes | Knowledge base ContentID |

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
