# openai.ChatCompletionNamedToolChoiceParam

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `any` | object | No |  |
| `function` | [openai.ChatCompletionNamedToolChoiceFunctionParam](openai-ChatCompletionNamedToolChoiceFunctionParam.md) | No |  |
| `type` | string | No | For function calling, the type is always `function`.

This field can be elided, and will marshal its zero value as "function". |

