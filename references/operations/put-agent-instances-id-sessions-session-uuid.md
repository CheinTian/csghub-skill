# PUT /agent/instances/{id}/sessions/{session_uuid}

**Resource:** [Agent](../resources/Agent.md)
**Update session by session UUID**
**Operation ID:** `put--agent-instances-{id}-sessions-{session_uuid}`

Update a session by session UUID

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | Instance ID |
| `session_uuid` | path | string | Yes | Session UUID |

## Request Body

Session data

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UpdateAgentInstanceSessionRequest](../schemas/types-UpdateAgentInstanceSessionRequest/types-UpdateAgentInstanceSessionRequest.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 403 | Forbidden |
| 500 | Internal server error |

## Security

- **ApiKey**
