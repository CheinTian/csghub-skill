# POST /v1/embeddings

**Resource:** [AIGateway](../resources/AIGateway.md)
**Get embedding for a text**
**Operation ID:** `post--v1-embeddings`

Sends a text to the backend model and returns the embedding

## Request Body

Embedding request

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [handler.EmbeddingRequest](../schemas/handler-EmbeddingRequest/handler-EmbeddingRequest.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request or sensitive input |
| 404 | Model not found |
| 500 | Internal server error |

**Success Response Schema:**

[types.Response](../schemas/types-Response/types-Response.md)

## Security

- **ApiKey**
