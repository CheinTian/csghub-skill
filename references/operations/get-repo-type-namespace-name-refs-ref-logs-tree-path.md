# GET /{repo_type}/{namespace}/{name}/refs/{ref}/logs_tree/{path}

**Resource:** [Repository](../resources/Repository.md)
**Get last commit for file tree**
**Operation ID:** `get--{repo_type}-{namespace}-{name}-refs-{ref}-logs_tree-{path}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `repo_type` | path | enum: models, datasets, codes... | Yes | models,dataset,codes or spaces |
| `namespace` | path | string | Yes | repo owner name |
| `name` | path | string | Yes | repo name |
| `path` | path | string | Yes | dir to list |
| `ref` | path | string | Yes | branch or tag |
| `limit` | query | integer | No | limit of records return |
| `offset` | query | integer | No | pagination offset |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
