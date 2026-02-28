# GET /agent/instances/{id}/sessions/{session_uuid}

**Resource:** [Agent](../resources/Agent.md)
**Get session by session UUID**
**Operation ID:** `get--agent-instances-{id}-sessions-{session_uuid}`

Get a session by session UUID

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | Instance ID |
| `session_uuid` | path | string | Yes | Session UUID |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
