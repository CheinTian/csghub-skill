# PUT /agent/knowledge-bases/{id}

**Resource:** [Agent](../resources/Agent.md)
**Update an existing agent knowledge base**
**Operation ID:** `put--agent-knowledge-bases-{id}`

Update the details of an existing agent knowledge base

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer (int64) | Yes | Knowledge base ID |

## Request Body

Updated knowledge base data

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UpdateAgentKnowledgeBaseRequest](../schemas/types-UpdateAgentKnowledgeBaseRequest/types-UpdateAgentKnowledgeBaseRequest.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 403 | Forbidden |
| 500 | Internal server error |

## Security

- **ApiKey**
