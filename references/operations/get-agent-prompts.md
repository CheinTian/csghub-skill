# GET /agent/prompts

**Resource:** [Agent](../resources/Agent.md)
**List agent prompts**
**Operation ID:** `get--agent-prompts`

Get all prompts for the current user with pin information and ordering

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `search` | query | string | No | Search term for path field |
| `per` | query | integer | No | Items per page |
| `page` | query | integer | No | Page number |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 401 | Unauthorized |
| 500 | Internal server error |

## Security

- **ApiKey**
