# POST /agent/prompts/optimize

**Resource:** [Agent](../resources/Agent.md)
**Optimize agent prompt**
**Operation ID:** `post--agent-prompts-optimize`

Optimize agent prompt content

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.AgentPromptOptimizeRequest](../schemas/types-AgentPromptOptimizeRequest/types-AgentPromptOptimizeRequest.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
