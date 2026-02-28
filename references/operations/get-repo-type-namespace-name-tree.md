# GET /{repo_type}/{namespace}/{name}/tree

**Resource:** [Repository](../resources/Repository.md)
**Get repository file tree**
**Operation ID:** `get--{repo_type}-{namespace}-{name}-tree`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `repo_type` | path | enum: models, datasets, codes... | Yes | models,dataset,codes or spaces |
| `namespace` | path | string | Yes | repo owner name |
| `name` | path | string | Yes | repo name |
| `path` | query | string | No | root dir |
| `ref` | query | string | No | branch or tag |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
