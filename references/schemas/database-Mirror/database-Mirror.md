# database.Mirror

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `created_at` | string | No |  |
| `current_task` | [database.MirrorTask](database-MirrorTask.md) | No |  |
| `current_task_id` | integer | No |  |
| `id` | integer | No |  |
| `interval` | string | No |  |
| `last_message` | string | No |  |
| `last_updated_at` | string | No |  |
| `local_repo_path` | string | No |  |
| `mirror_source` | [database.MirrorSource](database-MirrorSource.md) | No |  |
| `mirror_source_id` | integer | No |  |
| `mirror_task` | database.MirrorTask[] | No |  |
| `mirror_task_id` | integer | No |  |
| `next_execution_timestamp` | string | No |  |
| `priority` | [types.MirrorPriority](types-MirrorPriority.md) | No |  |
| `progress` | integer | No |  |
| `push_mirror_created` | boolean | No |  |
| `remote_updated_at` | string | No |  |
| `repository` | [database.Repository](database-Repository.md) | No |  |
| `repository_id` | integer | No |  |
| `retry_count` | integer | No |  |
| `source_repo_path` | string | No |  |
| `source_url` | string | No |  |
| `status` | [types.MirrorTaskStatus](types-MirrorTaskStatus.md) | No |  |
| `updated_at` | string | No |  |

