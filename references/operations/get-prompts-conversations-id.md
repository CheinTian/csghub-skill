# GET /prompts/conversations/{id}

**Resource:** [Prompt](../resources/Prompt.md)
**Get a conversation by uuid**
**Operation ID:** `get--prompts-conversations-{id}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | conversation uuid |

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
