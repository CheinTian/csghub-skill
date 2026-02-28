# PUT /prompts/conversations/{id}/message/{msgid}/hate

**Resource:** [Prompt](../resources/Prompt.md)
**Hate a conversation message**
**Operation ID:** `put--prompts-conversations-{id}-message-{msgid}-hate`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `uuid` | path | string | Yes | conversation uuid |
| `id` | path | string | Yes | message id |

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
