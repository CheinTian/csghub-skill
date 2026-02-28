# database.MirrorTask

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `after_last_commit_id` | string | No |  |
| `before_last_commit_id` | string | No |  |
| `created_at` | string | No |  |
| `error_message` | string | No |  |
| `finishedAt` | string | No |  |
| `id` | integer | No |  |
| `mirror` | [database.Mirror](database-Mirror.md) | No |  |
| `mirror_id` | integer | No |  |
| `payload` | string | No |  |
| `priority` | [types.MirrorPriority](types-MirrorPriority.md) | No |  |
| `progress` | integer | No |  |
| `retry_count` | integer | No |  |
| `startedAt` | string | No |  |
| `status` | [types.MirrorTaskStatus](types-MirrorTaskStatus.md) | No |  |
| `updated_at` | string | No |  |

