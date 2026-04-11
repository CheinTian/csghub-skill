# GET /{repo_type}/{namespace}/{name}/size/{branch}

**Resource:** [Repository](../resources/Repository.md)
**Get the repository size for a specific branch**
**Operation ID:** `get--{repo_type}-{namespace}-{name}-size-{branch}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `repo_type` | path | enum: models, datasets, codes... | Yes | models,datasets,codes,spaces or mcps |
| `namespace` | path | string | Yes | repo owner name |
| `name` | path | string | Yes | repo name |
| `branch` | path | string | Yes | branch name |
| `current_user` | query | string | No | current user name |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
