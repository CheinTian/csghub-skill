# GET /prompts/{namespace}/{name}/relations

**Resource:** [Prompt](../resources/Prompt.md)
**Get prompt related assets**
**Operation ID:** `get--prompts-{namespace}-{name}-relations`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `current_user` | query | string | No | current user |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
