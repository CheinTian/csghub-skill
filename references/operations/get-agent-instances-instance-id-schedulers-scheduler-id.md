# GET /agent/instances/{instance_id}/schedulers/{scheduler_id}

**Resource:** [Agent](../resources/Agent.md)
**Get agent scheduler by ID**
**Operation ID:** `get--agent-instances-{instance_id}-schedulers-{scheduler_id}`

Get details of a specific agent scheduler (must belong to the given instance)

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `instance_id` | path | integer | Yes | Agent instance ID |
| `scheduler_id` | path | integer | Yes | Scheduler ID |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 403 | Forbidden |
| 404 | Not found (scheduler not under this instance) |
| 500 | Internal server error |

## Security

- **ApiKey**
