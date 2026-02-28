# POST /admin/agent/configs

**Resource:** [Agent](../resources/Agent.md)
**Create Agent Config**
**Operation ID:** `post--admin-agent-configs`

Create a new agent system configuration

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreateAgentConfigReq](../schemas/types-CreateAgentConfigReq/types-CreateAgentConfigReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

