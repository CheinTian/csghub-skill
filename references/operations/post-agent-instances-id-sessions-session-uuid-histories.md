# POST /agent/instances/{id}/sessions/{session_uuid}/histories

**Resource:** [Agent](../resources/Agent.md)
**Create session histories for an agent instance session**
**Operation ID:** `post--agent-instances-{id}-sessions-{session_uuid}-histories`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | Instance ID |
| `session_uuid` | path | string | Yes | Session UUID |

## Request Body

Session history

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreateSessionHistoryRequest](../schemas/types-CreateSessionHistoryRequest/types-CreateSessionHistoryRequest.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
