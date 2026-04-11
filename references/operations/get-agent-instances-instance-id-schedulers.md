# GET /agent/instances/{instance_id}/schedulers

**Resource:** [Agent](../resources/Agent.md)
**List agent schedulers for an instance**
**Operation ID:** `get--agent-instances-{instance_id}-schedulers`

List all schedulers for the given agent instance with optional filters and pagination

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `instance_id` | path | integer | Yes | Agent instance ID |
| `status` | query | enum: active, paused, finished | No | filter by status |
| `schedule_type` | query | enum: once, daily, weekly... | No | filter by schedule type |
| `search` | query | string | No | search by scheduler name (partial, case-insensitive) |
| `not_finished` | query | boolean | No | exclude schedulers with status=finished |
| `per` | query | integer | No | page size |
| `page` | query | integer | No | current page number |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
