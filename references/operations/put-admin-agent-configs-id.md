# PUT /admin/agent/configs/:id

**Resource:** [Agent](../resources/Agent.md)
**Update Agent Config**
**Operation ID:** `put--admin-agent-configs-:id`

Update agent system configuration

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | Agent Config ID |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UpdateAgentConfigReq](../schemas/types-UpdateAgentConfigReq/types-UpdateAgentConfigReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

