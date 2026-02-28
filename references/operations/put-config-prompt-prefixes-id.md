# PUT /config/prompt_prefixes/{id}

**Resource:** [LLMService](../resources/LLMService.md)
**Update Prompt Config**
**Operation ID:** `put--config-prompt_prefixes-{id}`

Update existing prompt prefix by ID, supports partial updates of Chinese prompt (zh), English prompt (en) and kind fields. Return the updated prompt prefix. If the provided ID does not exist, it returns an error.

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | prompt_prefix.id |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UpdatePromptPrefixReq](../schemas/types-UpdatePromptPrefixReq/types-UpdatePromptPrefixReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

