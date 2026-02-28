# database.ArgoWorkflow

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `cluster_id` | string | No |  |
| `cluster_node` | string | No |  |
| `datasets` | string[] | No |  |
| `download_url` | string | No |  |
| `end_time` | string | No |  |
| `failures_url` | string | No |  |
| `id` | integer | No |  |
| `image` | string | No | ArgoWorkFlow framework |
| `namespace` | string | No |  |
| `queue_name` | string | No |  |
| `reason` | string | No | reason for status |
| `repo_ids` | string[] | No |  |
| `repo_type` | string | No |  |
| `resource_id` | integer | No |  |
| `resource_name` | string | No |  |
| `result_url` | string | No |  |
| `start_time` | string | No |  |
| `status` | [v1alpha1.WorkflowPhase](v1alpha1-WorkflowPhase.md) | No |  |
| `submit_time` | string | No |  |
| `task_desc` | string | No |  |
| `task_id` | string | No | generated task id |
| `task_name` | string | No | user input name |
| `task_type` | [types.TaskType](types-TaskType.md) | No |  |
| `user_uuid` | string | No |  |
| `username` | string | No |  |

