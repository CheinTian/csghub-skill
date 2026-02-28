# DELETE /config/prompt_prefixes/{id}

**Resource:** [LLMService](../resources/LLMService.md)
**Delete Prompt Config**
**Operation ID:** `delete--config-prompt_prefixes-{id}`

Use PromptPrefix.ID to Delete PromptPrefix in database

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

**Success Response Schema:**

[types.Response](../schemas/types-Response/types-Response.md)

