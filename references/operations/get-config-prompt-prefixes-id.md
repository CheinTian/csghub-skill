# GET /config/prompt_prefixes/{id}

**Resource:** [LLMService](../resources/LLMService.md)
**Get detail of prompt config by id**
**Operation ID:** `get--config-prompt_prefixes-{id}`

Use PromptPrefix.ID to retrieve in database

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | PromptPrefix.ID |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

