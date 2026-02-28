# GET /{repo_type}/{namespace}/{name}/commit/{commit_id}

**Resource:** [Repository](../resources/Repository.md)
**Get commit diff of repository and data field of response need to be decode with base64**
**Operation ID:** `get--{repo_type}-{namespace}-{name}-commit-{commit_id}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `repo_type` | path | enum: models, datasets, codes... | Yes | models,datasets,codes or spaces |
| `namespace` | path | string | Yes | repo owner name |
| `name` | path | string | Yes | repo name |
| `commit_id` | path | string | Yes | commit id |
| `current_user` | query | string | No | current user name |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
