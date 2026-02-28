# DELETE /config/llms/{id}

**Resource:** [LLMService](../resources/LLMService.md)
**Delete LLM Config**
**Operation ID:** `delete--config-llms-{id}`

Use LLMConfig.ID to delete LLM Config in database

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

**Success Response Schema:**

[types.Response](../schemas/types-Response/types-Response.md)

