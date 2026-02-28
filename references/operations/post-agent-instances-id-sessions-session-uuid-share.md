# POST /agent/instances/{id}/sessions/{session_uuid}/share

**Resource:** [Agent](../resources/Agent.md)
**Share a session**
**Operation ID:** `post--agent-instances-{id}-sessions-{session_uuid}-share`

Create a read-only shared session snapshot for an agent instance session

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
| 403 | Forbidden |
| 500 | Internal server error |

## Security

- **ApiKey**
