# types.FinetuneReq

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `agent` | string | No |  |
| `custom_args` | string | No |  |
| `dataset_id` | string | Yes |  |
| `epochs` | integer | No |  |
| `learning_rate` | number | No |  |
| `model_id` | string | Yes |  |
| `namespace` | string | No |  |
| `node_affinity` | [v1.NodeAffinity](v1-NodeAffinity.md) | No |  |
| `resource_id` | integer | Yes |  |
| `runtime_framework_id` | integer | Yes |  |
| `share_mode` | boolean | No |  |
| `task_desc` | string | No |  |
| `task_name` | string | No |  |
| `tolerations` | types.Toleration[] | No |  |

