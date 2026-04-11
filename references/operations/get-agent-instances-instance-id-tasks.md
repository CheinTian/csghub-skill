# GET /agent/instances/{instance_id}/tasks

**Resource:** [Agent](../resources/Agent.md)
**List scheduler tasks for an instance**
**Operation ID:** `get--agent-instances-{instance_id}-tasks`

List execution history (tasks) for all schedulers of an agent instance. Optionally filter by scheduler_id.

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `instance_id` | path | integer | Yes | Agent instance ID |
| `scheduler_id` | query | integer | No | filter by scheduler ID |
| `search` | query | string | No | search by task name (partial, case-insensitive) |
| `status` | query | enum: running, success, failed | No | filter by status |
| `per` | query | integer | No | page size |
| `page` | query | integer | No | current page number |

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
