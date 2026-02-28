# types.AgentTaskDetail

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `backend` | string | No | Backend system of the task (argo_workflow, deploy) |
| `created_at` | string | No |  |
| `id` | integer | No |  |
| `instance_id` | integer | No |  |
| `instance_name` | string | No |  |
| `instance_type` | string | No |  |
| `metadata` | object | No | Backend-specific fields (argo_workflow or deploy) |
| `session_name` | string | No |  |
| `session_uuid` | string | No |  |
| `status` | [types.AgentTaskStatus](types-AgentTaskStatus.md) | No |  |
| `task_desc` | string | No |  |
| `task_id` | string | No |  |
| `task_name` | string | No |  |
| `task_type` | [types.AgentTaskType](types-AgentTaskType.md) | No |  |
| `updated_at` | string | No |  |
| `username` | string | No |  |

