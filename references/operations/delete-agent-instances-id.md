# DELETE /agent/instances/{id}

**Resource:** [Agent](../resources/Agent.md)
**Delete an agent instance**
**Operation ID:** `delete--agent-instances-{id}`

Permanently delete an agent instance

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer (int64) | Yes | Instance ID |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 403 | Forbidden |
| 500 | Internal server error |

## Security

- **ApiKey**
