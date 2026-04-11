# POST /v1/images/generations

**Resource:** [AIGateway](../resources/AIGateway.md)
**Generate image from text prompt**
**Operation ID:** `post--v1-images-generations`

Generates images based on a text prompt

## Request Body

Image generation request

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [handler.ImageGenerationRequest](../schemas/handler-ImageGenerationRequest/handler-ImageGenerationRequest.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request or sensitive input |
| 404 | Model not found |
| 500 | Internal server error |

**Success Response Schema:**

[types.ImageGenerationResponse](../schemas/types-ImageGenerationResponse/types-ImageGenerationResponse.md)

## Security

- **ApiKey**
