# types.PromptRes

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `can_manage` | boolean | No |  |
| `can_write` | boolean | No |  |
| `created_at` | string | No |  |
| `csg_path` | string | No |  |
| `default_branch` | string | No |  |
| `description` | string | No |  |
| `downloads` | integer | No |  |
| `hf_path` | string | No |  |
| `id` | integer | No |  |
| `license` | string | No |  |
| `likes` | integer | No |  |
| `ms_path` | string | No |  |
| `name` | string | No |  |
| `namespace` | [types.Namespace](types-Namespace.md) | No |  |
| `nickname` | string | No |  |
| `path` | string | No |  |
| `private` | boolean | No |  |
| `readme` | string | No |  |
| `recom_op_weight` | integer | No |  |
| `repository` | [types.Repository](types-Repository.md) | No |  |
| `repository_id` | integer | No |  |
| `scores` | types.WeightScore[] | No |  |
| `sensitive_check_status` | string | No |  |
| `source` | [types.RepositorySource](types-RepositorySource.md) | No |  |
| `sync_status` | [types.RepositorySyncStatus](types-RepositorySyncStatus.md) | No |  |
| `tags` | types.RepoTag[] | No |  |
| `updated_at` | string | No |  |
| `user` | [types.User](types-User.md) | No |  |
| `user_likes` | boolean | No |  |

