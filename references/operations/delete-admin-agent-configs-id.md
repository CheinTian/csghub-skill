# DELETE /admin/agent/configs/:id

**Resource:** [Agent](../resources/Agent.md)
**Delete Agent Config**
**Operation ID:** `delete--admin-agent-configs-:id`

Delete an agent system configuration by ID

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | Agent Config ID |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

