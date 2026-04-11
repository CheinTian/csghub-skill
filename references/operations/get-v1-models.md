# GET /v1/models

**Resource:** [AIGateway](../resources/AIGateway.md)
**List available models**
**Operation ID:** `get--v1-models`

Returns a list of available models, supports fuzzy search by model_id query parameter and filtering by source and task

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `model_id` | query | string | No | Model ID for fuzzy search |
| `source` | query | enum: csghub, external | No | Filter by source (csghub for CSGHub models, external for external models) |
| `task` | query | string | No | Filter by task (e.g., text-generation, text-to-image) |
| `per` | query | integer | No | Models per page (default 20, max 100) |
| `page` | query | integer | No | Page number (1-based, default 1) |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Invalid source parameter |
| 500 | Internal server error |

**Success Response Schema:**

[types.ModelList](../schemas/types-ModelList/types-ModelList.md)

