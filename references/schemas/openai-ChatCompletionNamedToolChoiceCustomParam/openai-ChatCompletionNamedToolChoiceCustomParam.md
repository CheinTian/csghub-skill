# openai.ChatCompletionNamedToolChoiceCustomParam

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `any` | object | No |  |
| `custom` | [openai.ChatCompletionNamedToolChoiceCustomCustomParam](openai-ChatCompletionNamedToolChoiceCustomCustomParam.md) | No |  |
| `type` | string | No | For custom tool calling, the type is always `custom`.

This field can be elided, and will marshal its zero value as "custom". |

