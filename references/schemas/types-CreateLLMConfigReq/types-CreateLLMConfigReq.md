# types.CreateLLMConfigReq

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `api_endpoint` | string | Yes |  |
| `auth_header` | string | No |  |
| `enabled` | boolean | No |  |
| `metadata` | object | No | tasks stored as: {"tasks": ["text-generation", "text-to-image"]} |
| `model_name` | string | Yes |  |
| `official_name` | string | No |  |
| `provider` | string | Yes |  |
| `type` | integer | Yes | 1: optimization, 2: comparison, 4: summary readme, 8: mcp scan, 16: for aigateway call external llm |

