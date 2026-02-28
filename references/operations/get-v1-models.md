# GET /v1/models

**Resource:** [AIGateway](../resources/AIGateway.md)
**List available models**
**Operation ID:** `get--v1-models`

Returns a list of available models, supports fuzzy search by model_id query parameter and filtering by public status

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `model_id` | query | string | No | Model ID for fuzzy search |
| `public` | query | boolean | No | Filter by public status (true for public models, false for private models) |
| `per` | query | integer | No | Models per page (default 20, max 100) |
| `page` | query | integer | No | Page number (1-based, default 1) |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 500 | Internal server error |

**Success Response Schema:**

[types.ModelList](../schemas/types-ModelList/types-ModelList.md)

## Security

- **ApiKey**
