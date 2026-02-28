# GET /agent/templates/{id}/instances

**Resource:** [Agent](../resources/Agent.md)
**List agent instances by template ID**
**Operation ID:** `get--agent-templates-{id}-instances`

Get all agent instances created from a specific template

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `template_id` | path | integer (int64) | Yes | Template ID |
| `search` | query | string | No | search term |
| `type` | query | string | No | filter by type |
| `per` | query | integer | No | per |
| `page` | query | integer | No | per page |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 401 | Unauthorized |
| 500 | Internal server error |

## Security

- **ApiKey**
