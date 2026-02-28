# POST /agent/templates

**Resource:** [Agent](../resources/Agent.md)
**Create a new agent template**
**Operation ID:** `post--agent-templates`

## Request Body

Agent template data

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.AgentTemplate](../schemas/types-AgentTemplate/types-AgentTemplate.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
