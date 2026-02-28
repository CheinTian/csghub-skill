# PUT /prompts/conversations/{id}

**Resource:** [Prompt](../resources/Prompt.md)
**Update a conversation title**
**Operation ID:** `put--prompts-conversations-{id}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | conversation uuid |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.ConversationTitle](../schemas/types-ConversationTitle/types-ConversationTitle.md)

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
