# opencsg_com_csghub-server_common_types.Model

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `base_model` | string | No |  |
| `can_manage` | boolean | No |  |
| `can_write` | boolean | No |  |
| `created_at` | string | No |  |
| `csg_path` | string | No |  |
| `default_branch` | string | No |  |
| `description` | string | No |  |
| `disable_evaluation_reason` | string | No |  |
| `disable_finetune_reason` | string | No |  |
| `disable_inference_reason` | string | No |  |
| `downloads` | integer | No |  |
| `enable_evaluation` | boolean | No |  |
| `enable_finetune` | boolean | No |  |
| `enable_inference` | boolean | No |  |
| `hf_path` | string | No |  |
| `high_risk_count` | integer | No |  |
| `id` | integer | No |  |
| `license` | string | No |  |
| `likes` | integer | No |  |
| `medium_risk_count` | integer | No |  |
| `metadata` | [types.Metadata](types-Metadata.md) | No |  |
| `mirror_last_updated_at` | string | No |  |
| `mirror_task_status` | [types.MirrorTaskStatus](types-MirrorTaskStatus.md) | No |  |
| `ms_path` | string | No |  |
| `name` | string | No |  |
| `namespace` | [types.Namespace](types-Namespace.md) | No |  |
| `nickname` | string | No |  |
| `path` | string | No |  |
| `private` | boolean | No |  |
| `readme` | string | No |  |
| `recom_op_weight` | integer | No |  |
| `report_url` | string | No |  |
| `repository` | [types.Repository](types-Repository.md) | No |  |
| `repository_id` | integer | No |  |
| `scores` | types.WeightScore[] | No |  |
| `sensitive_check_status` | string | No |  |
| `source` | [types.RepositorySource](types-RepositorySource.md) | No |  |
| `status` | string | No | url to interact with the model |
| `sync_status` | [types.RepositorySyncStatus](types-RepositorySyncStatus.md) | No |  |
| `tags` | types.RepoTag[] | No |  |
| `updated_at` | string | No |  |
| `url` | string | No |  |
| `user` | [types.User](types-User.md) | No |  |
| `user_likes` | boolean | No |  |
| `widget_type` | object | No | widget UI style: generation,chat |
| `xnet_enabled` | boolean | No |  |
| `xnet_migration_progress` | integer | No |  |
| `xnet_migration_status` | [types.XnetMigrationTaskStatus](types-XnetMigrationTaskStatus.md) | No |  |

