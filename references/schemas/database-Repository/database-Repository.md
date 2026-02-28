# database.Repository

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `created_at` | string | No |  |
| `csg_path` | string | No |  |
| `current_xnet_migration_task` | [database.XnetMigrationTask](database-XnetMigrationTask.md) | No |  |
| `current_xnet_migration_task_id` | integer | No |  |
| `default_branch` | string | No |  |
| `deletedAt` | string | No |  |
| `description` | string | No |  |
| `download_count` | integer | No |  |
| `downloads` | database.RepositoryDownload[] | No |  |
| `git_path` | string | No |  |
| `github_path` | string | No |  |
| `hashed` | boolean | No |  |
| `hf_path` | string | No |  |
| `http_clone_url` | string | No |  |
| `id` | integer | No |  |
| `labels` | string | No | Depreated |
| `lfs_objects_size` | integer | No |  |
| `license` | string | No |  |
| `likes` | integer | No |  |
| `metadata` | [database.Metadata](database-Metadata.md) | No |  |
| `migrated` | boolean | No |  |
| `mirror` | [database.Mirror](database-Mirror.md) | No |  |
| `ms_path` | string | No |  |
| `name` | string | No |  |
| `nickname` | string | No |  |
| `path` | string | No |  |
| `private` | boolean | No |  |
| `readme` | string | No | Depreated |
| `repository_type` | [types.RepositoryType](types-RepositoryType.md) | No |  |
| `sensitive_check_status` | [types.SensitiveCheckStatus](types-SensitiveCheckStatus.md) | No |  |
| `source` | [types.RepositorySource](types-RepositorySource.md) | No |  |
| `ssh_clone_url` | string | No |  |
| `star_count` | integer | No |  |
| `sync_status` | object | No | Only used for multi-source sync status |
| `tags` | database.Tag[] | No |  |
| `updated_at` | string | No |  |
| `user` | [database.User](database-User.md) | No |  |
| `user_id` | integer | No |  |
| `xnet_enabled` | boolean | No |  |

