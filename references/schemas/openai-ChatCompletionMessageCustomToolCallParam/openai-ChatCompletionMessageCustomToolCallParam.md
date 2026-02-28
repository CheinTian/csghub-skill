# openai.ChatCompletionMessageCustomToolCallParam

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `any` | object | No |  |
| `custom` | object | No | The custom tool that the model called. |
| `id` | string | No | The ID of the tool call. |
| `type` | string | No | The type of the tool. Always `custom`.

This field can be elided, and will marshal its zero value as "custom". |

