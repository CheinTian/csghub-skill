# POST /agent/instances/{instance_id}/schedulers/{scheduler_id}/execute

**Resource:** [Agent](../resources/Agent.md)
**Execute scheduler now**
**Operation ID:** `post--agent-instances-{instance_id}-schedulers-{scheduler_id}-execute`

Create and return a new scheduler task (run once). Scheduler must belong to the given instance. Returns the created task in the response body.

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
| 404 | Not found |
| 500 | Internal server error |

## Security

- **ApiKey**
