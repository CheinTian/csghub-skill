# POST /v1/chat/completions

**Resource:** [AIGateway](../resources/AIGateway.md)
**Chat with backend model**
**Operation ID:** `post--v1-chat-completions`

Sends a chat completion request to the backend model and returns the response

## Request Body

Chat completion request

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [handler.ChatCompletionRequest](../schemas/handler-ChatCompletionRequest/handler-ChatCompletionRequest.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 404 | Model not found |
| 500 | Internal server error |

**Success Response Schema:**

[openai.ChatCompletionChunk](../schemas/openai-ChatCompletionChunk/openai-ChatCompletionChunk.md)

## Security

- **ApiKey**
