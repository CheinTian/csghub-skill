# GET /{repo_type}/{namespace}/{name}/blob/{file_path}

**Resource:** [Repository](../resources/Repository.md)
**Get the repo file information like size, content, sha etc**
**Operation ID:** `get--{repo_type}-{namespace}-{name}-blob-{file_path}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `repo_type` | path | enum: models, datasets, codes... | Yes | models,dataset,codes or spaces |
| `namespace` | path | string | Yes | repo owner name |
| `name` | path | string | Yes | repo name |
| `file_path` | path | string | Yes | file path |
| `ref` | query | string | Yes | branch or tag |
| `current_user` | query | string | No | current user name |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey or JWT**
