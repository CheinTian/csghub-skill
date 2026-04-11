# types.InstanceRunReq

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `cluster_id` | string | No |  |
| `deploy_name` | string | No |  |
| `engine_args` | string | No |  |
| `order_detail_id` | integer | No |  |
| `owner_namespace` | string | No | OwnerNamespace is optional. If set, the finetune is created under this namespace (user or org); path {namespace} remains the model's owner. |
| `resource_id` | integer | No |  |
| `revision` | string | No |  |
| `runtime_framework_id` | integer | No |  |

