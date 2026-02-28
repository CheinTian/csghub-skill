# PUT /agent/knowledge-bases/content-id/{content_id}

**Resource:** [Agent](../resources/Agent.md)
**Update an agent knowledge base by ContentID**
**Operation ID:** `put--agent-knowledge-bases-content-id-{content_id}`

Update the details of an existing agent knowledge base by its content ID

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `content_id` | path | string | Yes | Knowledge base ContentID |

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
