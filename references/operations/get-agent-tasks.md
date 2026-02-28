# GET /agent/tasks

**Resource:** [Agent](../resources/Agent.md)
**List agent tasks**
**Operation ID:** `get--agent-tasks`

List all agent tasks for the current user with filtering and pagination

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `search` | query | string | No | search by task name |
| `task_type` | query | enum: finetuneJob, inference | No | filter by task type |
| `status` | query | enum: in_progress, completed, failed | No | filter by status |
| `instance_id` | query | integer | No | filter by instance ID |
| `session_uuid` | query | string | No | filter by session UUID |
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
