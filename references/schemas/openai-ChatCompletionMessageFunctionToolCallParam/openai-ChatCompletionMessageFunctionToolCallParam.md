# openai.ChatCompletionMessageFunctionToolCallParam

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `any` | object | No |  |
| `function` | object | No | The function that the model called. |
| `id` | string | No | The ID of the tool call. |
| `type` | string | No | The type of the tool. Currently, only `function` is supported.

This field can be elided, and will marshal its zero value as "function". |

