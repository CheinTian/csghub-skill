# openai.ChatCompletionToolMessageParam

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `any` | object | No |  |
| `content` | object | No | The contents of the tool message. |
| `role` | string | No | The role of the messages author, in this case `tool`.

This field can be elided, and will marshal its zero value as "tool". |
| `tool_call_id` | string | No | Tool call that this message is responding to. |

