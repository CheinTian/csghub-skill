# handler.ChatCompletionRequest

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `max_tokens` | integer | No |  |
| `messages` | openai.ChatCompletionMessageParamUnion[] | No |  |
| `model` | string | No |  |
| `stream` | boolean | No |  |
| `stream_options` | [handler.StreamOptions](handler-StreamOptions.md) | No |  |
| `temperature` | number | No |  |
| `tool_choice` | object | No | Controls which (if any) tool is called by the model. `none` means the model will
not call any tool and instead generates a message. `auto` means the model can
pick between generating a message or calling one or more tools. `required` means
the model must call one or more tools. Specifying a particular tool via
`{"type": "function", "function": {"name": "my_function"}}` forces the model to
call that tool.

`none` is the default when no tools are present. `auto` is the default if tools
are present. |
| `tools` | openai.ChatCompletionToolUnionParam[] | No | A list of tools the model may call. You can provide either
[custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)
or [function tools](https://platform.openai.com/docs/guides/function-calling). |

