# GET /agent/instances/{id}/sessions/{session_uuid}/histories

**Resource:** [Agent](../resources/Agent.md)
**List session histories by session UUID**
**Operation ID:** `get--agent-instances-{id}-sessions-{session_uuid}-histories`

List all session histories for a specific session

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | Instance ID |
| `session_uuid` | path | string | Yes | Session UUID |
| `max_turn` | query | integer | No | Max turn number |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
