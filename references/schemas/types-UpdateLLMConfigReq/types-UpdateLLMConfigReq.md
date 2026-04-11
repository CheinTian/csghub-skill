# types.UpdateLLMConfigReq

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `api_endpoint` | string | No |  |
| `auth_header` | string | No |  |
| `enabled` | boolean | No |  |
| `id` | integer | No |  |
| `metadata` | object | No | tasks stored as: {"tasks": ["text-generation", "text-to-image"]} |
| `model_name` | string | No |  |
| `official_name` | string | No |  |
| `provider` | string | No |  |
| `type` | integer | No | 1: optimization, 2: comparison, 4: summary readme |

