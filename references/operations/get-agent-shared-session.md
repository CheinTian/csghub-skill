# GET /agent/shared/session

**Resource:** [Agent](../resources/Agent.md)
**Get shared session by share uuid**
**Operation ID:** `get--agent-shared-session`

Fetch a read-only shared session snapshot by share uuid

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `share_uuid` | query | string | Yes | Share UUID |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 404 | Not found |
| 410 | Gone |
| 500 | Internal server error |

