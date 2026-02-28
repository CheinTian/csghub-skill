# openai.ChatCompletionFunctionToolParam

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `any` | object | No |  |
| `function` | [shared.FunctionDefinitionParam](shared-FunctionDefinitionParam.md) | No |  |
| `type` | string | No | The type of the tool. Currently, only `function` is supported.

This field can be elided, and will marshal its zero value as "function". |

