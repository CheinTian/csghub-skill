# openai.ChatCompletionAllowedToolsParam

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `any` | object | No |  |
| `mode` | object | No | Constrains the tools available to the model to a pre-defined set.

`auto` allows the model to pick from among the allowed tools and generate a
message.

`required` requires the model to call one or more of the allowed tools.

Any of "auto", "required". |
| `tools` | object[] | No | A list of tool definitions that the model should be allowed to call.

For the Chat Completions API, the list of tool definitions might look like:

```json
[

	{ "type": "function", "function": { "name": "get_weather" } },
	{ "type": "function", "function": { "name": "get_time" } }

]
``` |

