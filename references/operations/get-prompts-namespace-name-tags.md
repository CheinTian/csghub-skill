# GET /prompts/{namespace}/{name}/tags

**Resource:** [Prompt](../resources/Prompt.md)
**Get the tags of prompt repository**
**Operation ID:** `get--prompts-{namespace}-{name}-tags`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | repo owner name |
| `name` | path | string | Yes | repo name |
| `current_user` | query | string | No | current user name |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
