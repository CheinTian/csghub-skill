# openai.ChatCompletionToolChoiceOptionUnionParam

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `any` | object | No |  |
| `ofAllowedTools` | [openai.ChatCompletionAllowedToolChoiceParam](openai-ChatCompletionAllowedToolChoiceParam.md) | No |  |
| `ofAuto` | object | No | Check if union is this variant with !param.IsOmitted(union.OfAuto) |
| `ofCustomToolChoice` | [openai.ChatCompletionNamedToolChoiceCustomParam](openai-ChatCompletionNamedToolChoiceCustomParam.md) | No |  |
| `ofFunctionToolChoice` | [openai.ChatCompletionNamedToolChoiceParam](openai-ChatCompletionNamedToolChoiceParam.md) | No |  |

