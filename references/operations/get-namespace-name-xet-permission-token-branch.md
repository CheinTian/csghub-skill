# GET /{namespace}/{name}/xet-{permission}-token/{branch}

**Resource:** [User](../resources/User.md)
**Get xnet write token**
**Operation ID:** `get--{namespace}-{name}-xet-{permission}-token-{branch}`

get xnet write token

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `branch` | path | string | Yes | branch |
| `permission` | path | enum: write, read | Yes | permission |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
