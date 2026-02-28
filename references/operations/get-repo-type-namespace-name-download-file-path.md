# GET /{repo_type}/{namespace}/{name}/download/{file_path}

**Resource:** [Repository](../resources/Repository.md)
**Download a repo file [Depricated: use 'resolve' api instead]**
**Operation ID:** `get--{repo_type}-{namespace}-{name}-download-{file_path}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `repo_type` | path | enum: models, datasets, codes... | Yes | models,dataset,codes or spaces |
| `namespace` | path | string | Yes | repo owner name |
| `name` | path | string | Yes | repo name |
| `file_path` | path | string | Yes | file path |
| `ref` | query | string | No | branch or tag |
| `save_as` | query | string | No | file name to save as |
| `current_user` | query | string | No | current user name |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey or JWT**
