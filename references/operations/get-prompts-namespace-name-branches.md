# GET /prompts/{namespace}/{name}/branches

**Resource:** [Prompt](../resources/Prompt.md)
**Get the branches of prompt repository**
**Operation ID:** `get--prompts-{namespace}-{name}-branches`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | repo owner name |
| `name` | path | string | Yes | repo name |
| `ref` | query | string | Yes | branch or tag |
| `current_user` | query | string | No | current user name |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
