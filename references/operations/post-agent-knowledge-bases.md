# POST /agent/knowledge-bases

**Resource:** [Agent](../resources/Agent.md)
**Create a new agent knowledge base**
**Operation ID:** `post--agent-knowledge-bases`

Create a new agent knowledge base configuration

## Request Body

Create agent knowledge base request

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreateAgentKnowledgeBaseReq](../schemas/types-CreateAgentKnowledgeBaseReq/types-CreateAgentKnowledgeBaseReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
