# database.Deploy

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `annotation` | string | No |  |
| `cluster_id` | string | No |  |
| `cluster_node` | string | No |  |
| `container_port` | integer | No |  |
| `created_at` | string | No |  |
| `deploy_name` | string | No | add at 2024-05 |
| `endpoint` | string | No |  |
| `engine_args` | string | No |  |
| `env` | string | No |  |
| `git_branch` | string | No |  |
| `git_path` | string | No |  |
| `hardware` | string | No |  |
| `id` | integer | No |  |
| `image_id` | string | No | for image run task, aka task_type = 1
running image of cluster, comes from builder or pre-define |
| `max_replica` | integer | No |  |
| `message` | string | No |  |
| `min_replica` | integer | No |  |
| `model_id` | integer | No | model_id to deploy, it's 0 if deploy space |
| `order_detail_id` | integer | No |  |
| `queue_name` | string | No |  |
| `reason` | string | No |  |
| `repo_id` | integer | No | repository_id of model/space/code/dataset |
| `repository` | [database.Repository](database-Repository.md) | No |  |
| `runtime_framework` | string | No | model running engine vllm or TGI |
| `secret` | string | No |  |
| `secure_level` | integer | No | 1-public, 2-private, 3-extension in future |
| `sku` | string | No |  |
| `space_id` | integer | No | space_id to deploy, it's 0 if deploy model |
| `status` | integer | No |  |
| `svc_name` | string | No |  |
| `task` | object | No | text-generation,text-to-image,text-to-speech |
| `template` | string | No |  |
| `type` | integer | No | 0-space, 1-inference, 2-finetune, 3-serverless, 4-evaluation, 5-notebook |
| `updated_at` | string | No |  |
| `user` | [database.User](database-User.md) | No |  |
| `user_id` | integer | No | user_id trigger deploy action, rather than repo owner user_id |
| `user_uuid` | string | No |  |
| `variables` | string | No |  |

