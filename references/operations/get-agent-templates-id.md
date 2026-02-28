# GET /agent/templates/{id}

**Resource:** [Agent](../resources/Agent.md)
**Get an agent template by ID**
**Operation ID:** `get--agent-templates-{id}`

Get details of a specific agent template

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer (int64) | Yes | Template ID |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
