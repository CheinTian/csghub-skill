# openai.ChatCompletionFunctionMessageParam

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `any` | object | No |  |
| `content` | object | No | The contents of the function message. |
| `name` | string | No | The name of the function to call. |
| `role` | string | No | The role of the messages author, in this case `function`.

This field can be elided, and will marshal its zero value as "function". |

