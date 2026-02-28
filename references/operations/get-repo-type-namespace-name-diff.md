# GET /{repo_type}/{namespace}/{name}/diff

**Resource:** [Repository](../resources/Repository.md)
**Get commit diff of repository and data field of response need to be decode with base64**
**Operation ID:** `get--{repo_type}-{namespace}-{name}-diff`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `repo_type` | path | enum: models, datasets, codes... | Yes | models,datasets,codes or spaces |
| `namespace` | path | string | Yes | repo owner name |
| `name` | path | string | Yes | repo name |
| `current_user` | query | string | No | current user name |
| `left_commit_id` | query | string | Yes | previous commit id |
| `right_commit_id` | query | string | No | current commit id |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
