# GET /{repo_type}/{namespace}/{name}/discussions

**Resource:** [Discussion](../resources/Discussion.md)
**List repo discussions**
**Operation ID:** `get--{repo_type}-{namespace}-{name}-discussions`

list repo discussions

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `per` | query | integer | No | per |
| `page` | query | integer | No | per page |
| `current_user` | query | string | No | current user |
| `repo_type` | path | enum: models, datasets, codes... | Yes | repository type |
| `namespace` | path | string | Yes | namespace |
| `name` | query | string | Yes | name |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
