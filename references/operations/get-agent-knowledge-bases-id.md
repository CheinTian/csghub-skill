# GET /agent/knowledge-bases/{id}

**Resource:** [Agent](../resources/Agent.md)
**Get an agent knowledge base by ID**
**Operation ID:** `get--agent-knowledge-bases-{id}`

Get details of a specific agent knowledge base

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

## Security

- **ApiKey**
