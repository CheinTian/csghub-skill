# POST /agent/instances/{id}/sessions

**Resource:** [Agent](../resources/Agent.md)
**Create a new session for an agent instance**
**Operation ID:** `post--agent-instances-{id}-sessions`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | Instance ID |

## Request Body

Session data

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreateAgentInstanceSessionRequest](../schemas/types-CreateAgentInstanceSessionRequest/types-CreateAgentInstanceSessionRequest.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
