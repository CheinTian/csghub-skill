# openai.ChatCompletionDeveloperMessageParam

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `any` | object | No |  |
| `content` | object | No | The contents of the developer message. |
| `name` | object | No | An optional name for the participant. Provides the model information to
differentiate between participants of the same role. |
| `role` | string | No | The role of the messages author, in this case `developer`.

This field can be elided, and will marshal its zero value as "developer". |

