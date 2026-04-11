# GET /agent/skills

**Resource:** [Agent](../resources/Agent.md)
**List agent skills (platform + user-created)**
**Operation ID:** `get--agent-skills`

list agent skills including platform skills with 'agentichub-skills' tag and user-created skills

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `current_user` | query | string | No | current user |
| `search` | query | string | No | search text |
| `built_in` | query | boolean | No | filter: true=platform skills only, false=user-created only |
| `per` | query | integer | No | per |
| `page` | query | integer | No | page |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
