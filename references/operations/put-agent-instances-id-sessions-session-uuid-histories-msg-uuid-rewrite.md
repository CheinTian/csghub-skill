# PUT /agent/instances/{id}/sessions/{session_uuid}/histories/{msg_uuid}/rewrite

**Resource:** [Agent](../resources/Agent.md)
**Rewrite an output message**
**Operation ID:** `put--agent-instances-{id}-sessions-{session_uuid}-histories-{msg_uuid}-rewrite`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | Instance ID |
| `session_uuid` | path | string | Yes | Session UUID |
| `msg_uuid` | path | string | Yes | Message UUID |

## Request Body

Rewrite session history request

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.RewriteSessionHistoryRequest](../schemas/types-RewriteSessionHistoryRequest/types-RewriteSessionHistoryRequest.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
