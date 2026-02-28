# opencsg_com_csghub-server_aigateway_types.Model

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `created` | integer | No | organization-owner (e.g. openai) |
| `endpoint` | string | No |  |
| `id` | string | No |  |
| `is_pinned` | boolean | No | whether the model is pinned |
| `object` | string | No |  |
| `owned_by` | string | No |  |
| `public` | boolean | No | whether the model is public (false = private, true = public) |
| `support_function_call` | boolean | No | whether the model supports function calling |
| `task` | string | No | like text-generation, text-to-image etc |

