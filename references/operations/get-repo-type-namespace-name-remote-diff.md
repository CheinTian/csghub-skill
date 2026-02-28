# GET /{repo_type}/{namespace}/{name}/remote_diff

**Resource:** [Repository](../resources/Repository.md)
**Get diff between local last commit and remote commit**
**Operation ID:** `get--{repo_type}-{namespace}-{name}-remote_diff`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `repo_type` | path | enum: models, datasets, codes... | Yes | models,datasets,codes or spaces |
| `namespace` | path | string | Yes | repo owner name |
| `name` | path | string | Yes | repo name |
| `current_user` | query | string | No | current user name |
| `left_commit_id` | query | string | Yes | previous commit id |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
