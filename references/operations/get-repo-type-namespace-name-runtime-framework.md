# GET /{repo_type}/{namespace}/{name}/runtime_framework

**Resource:** [RuntimeFramework](../resources/RuntimeFramework.md)
**[Deprecated: use GET:/{repo_type}/{namespace}/{name}/runtime_framework_v2 instead]**
**Operation ID:** `get--{repo_type}-{namespace}-{name}-runtime_framework`

List repo runtime framework

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
