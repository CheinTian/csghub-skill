# types.Space

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `can_manage` | boolean | No |  |
| `can_write` | boolean | No |  |
| `cluster_id` | string | No |  |
| `cover_image_url` | string | No |  |
| `created_at` | string | No |  |
| `default_branch` | string | No |  |
| `deploy_id` | integer | No |  |
| `description` | string | No |  |
| `driver_version` | string | No |  |
| `endpoint` | string | No | the serving endpoint url |
| `env` | string | No |  |
| `hardware` | string | No |  |
| `id` | integer | No |  |
| `instances` | types.Instance[] | No |  |
| `license` | string | No |  |
| `like_count` | integer | No |  |
| `min_replica` | integer | No |  |
| `name` | string | No |  |
| `namespace` | [types.Namespace](types-Namespace.md) | No |  |
| `nickname` | string | No |  |
| `path` | string | No |  |
| `private` | boolean | No |  |
| `recom_op_weight` | integer | No |  |
| `repository` | [types.Repository](types-Repository.md) | No |  |
| `repository_id` | integer | No |  |
| `sdk` | string | No | like gradio,steamlit etc |
| `sdk_version` | string | No |  |
| `secrets` | string | No |  |
| `sensitive_check_status` | string | No |  |
| `sku` | string | No |  |
| `source` | [types.RepositorySource](types-RepositorySource.md) | No |  |
| `status` | string | No | deploying, running, failed |
| `svc_name` | string | No |  |
| `sync_status` | [types.RepositorySyncStatus](types-RepositorySyncStatus.md) | No |  |
| `tags` | types.RepoTag[] | No |  |
| `template` | string | No |  |
| `updated_at` | string | No |  |
| `user` | [types.User](types-User.md) | No |  |
| `user_likes` | boolean | No |  |
| `username` | string | No |  |
| `variables` | string | No |  |

