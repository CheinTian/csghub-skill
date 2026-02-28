# GET /{repo_type}/{namespace}/{name}/tags

**Resource:** [Repository](../resources/Repository.md)
**Get the tags of repository**
**Operation ID:** `get--{repo_type}-{namespace}-{name}-tags`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `repo_type` | path | enum: models, datasets, codes... | Yes | models,dataset,codes or spaces |
| `namespace` | path | string | Yes | repo owner name |
| `name` | path | string | Yes | repo name |
| `current_user` | query | string | No | current user name |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
