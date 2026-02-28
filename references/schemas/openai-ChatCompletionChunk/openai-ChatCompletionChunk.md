# openai.ChatCompletionChunk

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `choices` | openai.ChatCompletionChunkChoice[] | No | A list of chat completion choices. Can contain more than one elements if `n` is
greater than 1. Can also be empty for the last chunk if you set
`stream_options: {"include_usage": true}`. |
| `created` | integer | No | The Unix timestamp (in seconds) of when the chat completion was created. Each
chunk has the same timestamp. |
| `id` | string | No | A unique identifier for the chat completion. Each chunk has the same ID. |
| `model` | string | No | The model to generate the completion. |
| `object` | string | No | The object type, which is always `chat.completion.chunk`. |
| `service_tier` | object | No | Specifies the processing type used for serving the request.

  - If set to 'auto', then the request will be processed with the service tier
    configured in the Project settings. Unless otherwise configured, the Project
    will use 'default'.
  - If set to 'default', then the request will be processed with the standard
    pricing and performance for the selected model.
  - If set to '[flex](https://platform.openai.com/docs/guides/flex-processing)' or
    '[priority](https://openai.com/api-priority-processing/)', then the request
    will be processed with the corresponding service tier.
  - When not set, the default behavior is 'auto'.

When the `service_tier` parameter is set, the response body will include the
`service_tier` value based on the processing mode actually used to serve the
request. This response value may be different from the value set in the
parameter.

Any of "auto", "default", "flex", "scale", "priority". |
| `system_fingerprint` | string | No | This fingerprint represents the backend configuration that the model runs with.
Can be used in conjunction with the `seed` request parameter to understand when
backend changes have been made that might impact determinism.

Deprecated: deprecated |
| `usage` | object | No | An optional field that will only be present when you set
`stream_options: {"include_usage": true}` in your request. When present, it
contains a null value **except for the last chunk** which contains the token
usage statistics for the entire request.

**NOTE:** If the stream is interrupted or cancelled, you may not receive the
final usage chunk which contains the total token usage for the request. |

