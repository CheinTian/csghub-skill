# openai.ChatCompletionAllowedToolChoiceParam

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `allowed_tools` | object | No | Constrains the tools available to the model to a pre-defined set. |
| `any` | object | No |  |
| `type` | string | No | Allowed tool configuration type. Always `allowed_tools`.

This field can be elided, and will marshal its zero value as "allowed_tools". |

