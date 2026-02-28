# DELETE /agent/instances/by-content-id/{type}/{content_id}

**Resource:** [Agent](../resources/Agent.md)
**Delete an agent instance by type and content id**
**Operation ID:** `delete--agent-instances-by-content-id-{type}-{content_id}`

Permanently delete an agent instance by type and content id

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `type` | path | string | Yes | type |
| `content_id` | path | string | Yes | content id |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 403 | Forbidden |
| 500 | Internal server error |

## Security

- **ApiKey**
