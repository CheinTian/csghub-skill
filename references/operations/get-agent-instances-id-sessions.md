# GET /agent/instances/{id}/sessions

**Resource:** [Agent](../resources/Agent.md)
**List sessions by instance ID**
**Operation ID:** `get--agent-instances-{id}-sessions`

List all sessions for a specific agent instance with pagination

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | Instance ID |
| `per` | query | integer | No | page size |
| `page` | query | integer | No | current page number |
| `search` | query | string | No | search by session name |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
