# GET /agent/instances/{id}

**Resource:** [Agent](../resources/Agent.md)
**Get an agent instance by ID**
**Operation ID:** `get--agent-instances-{id}`

Get details of a specific agent instance

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer (int64) | Yes | Instance ID |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
