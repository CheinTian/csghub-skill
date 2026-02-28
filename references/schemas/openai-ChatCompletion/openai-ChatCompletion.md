# openai.ChatCompletion

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `choices` | openai.ChatCompletionChoice[] | No | A list of chat completion choices. Can be more than one if `n` is greater
than 1. |
| `created` | integer | No | The Unix timestamp (in seconds) of when the chat completion was created. |
| `id` | string | No | A unique identifier for the chat completion. |
| `model` | string | No | The model used for the chat completion. |
| `object` | string | No | The object type, which is always `chat.completion`. |
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
| `usage` | object | No | Usage statistics for the completion request. |

