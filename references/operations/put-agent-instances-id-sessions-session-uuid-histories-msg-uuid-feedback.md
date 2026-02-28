# PUT /agent/instances/{id}/sessions/{session_uuid}/histories/{msg_uuid}/feedback

**Resource:** [Agent](../resources/Agent.md)
**Update the feedback of a session history message**
**Operation ID:** `put--agent-instances-{id}-sessions-{session_uuid}-histories-{msg_uuid}-feedback`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | Instance ID |
| `session_uuid` | path | string | Yes | Session UUID |
| `msg_uuid` | path | string | Yes | Message UUID |

## Request Body

feedback for session history message

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.FeedbackSessionHistoryRequest](../schemas/types-FeedbackSessionHistoryRequest/types-FeedbackSessionHistoryRequest.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
