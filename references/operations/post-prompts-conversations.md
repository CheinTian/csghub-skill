# POST /prompts/conversations

**Resource:** [Prompt](../resources/Prompt.md)
**Create new conversation**
**Operation ID:** `post--prompts-conversations`

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.Conversation](../schemas/types-Conversation/types-Conversation.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

**Success Response Schema:**

[types.Response](../schemas/types-Response/types-Response.md)

## Security

- **ApiKey**
