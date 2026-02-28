# PUT /prompts/{namespace}/{name}/prompt/file/{file_path}

**Resource:** [Prompt](../resources/Prompt.md)
**Update prompt in repo**
**Operation ID:** `put--prompts-{namespace}-{name}-prompt-file-{file_path}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `file_path` | path | string | Yes | the file relative path |
| `current_user` | query | string | No | current user name |

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
