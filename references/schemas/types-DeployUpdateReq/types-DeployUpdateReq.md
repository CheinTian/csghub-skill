# types.DeployUpdateReq

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `cluster_id` | string | No |  |
| `deploy_name` | string | No |  |
| `engine_args` | string | No |  |
| `entrypoint` | string | No |  |
| `env` | string | No |  |
| `max_replica` | integer | No |  |
| `min_replica` | integer | No |  |
| `node_affinity` | [v1.NodeAffinity](v1-NodeAffinity.md) | No |  |
| `resource_id` | integer | No |  |
| `revision` | string | No |  |
| `runtime_framework_id` | integer | No |  |
| `secure_level` | integer | No |  |
| `tolerations` | types.Toleration[] | No |  |
| `variables` | string | No |  |

