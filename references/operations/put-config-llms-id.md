# PUT /config/llms/{id}

**Resource:** [LLMService](../resources/LLMService.md)
**Update LLM Config**
**Operation ID:** `put--config-llms-{id}`

Update existing LLM configuration by ID. If input ModelName, ApiEndpoint, AuthHeader, Type, Enabled not null, update in database. Return the updated LLM configuration. If the provided ID does not exist, it returns an error.

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | id |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UpdateLLMConfigReq](../schemas/types-UpdateLLMConfigReq/types-UpdateLLMConfigReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

