# GET /config/llms/{id}

**Resource:** [LLMService](../resources/LLMService.md)
**Get detail of llm config by id**
**Operation ID:** `get--config-llms-{id}`

Use LLMConfig.ID to retrieve in database

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | LLMConfig.ID |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

