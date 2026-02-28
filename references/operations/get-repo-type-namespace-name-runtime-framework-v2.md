# GET /{repo_type}/{namespace}/{name}/runtime_framework_v2

**Resource:** [RuntimeFramework](../resources/RuntimeFramework.md)
**List repo runtime framework**
**Operation ID:** `get--{repo_type}-{namespace}-{name}-runtime_framework_v2`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `repo_type` | path | enum: models, spaces | Yes | models,spaces |
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `current_user` | query | string | No | current user |
| `deploy_type` | query | enum: 0, 1, 2... | No | deploy_type |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
