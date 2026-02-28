# GET /{repo_type}/{namespace}/{name}/run/{id}

**Resource:** [Repository](../resources/Repository.md)
**Get repo deploy detail**
**Operation ID:** `get--{repo_type}-{namespace}-{name}-run-{id}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `repo_type` | path | enum: models, spaces | Yes | models,spaces |
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `id` | path | string | Yes | id |
| `current_user` | query | string | No | current user |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 401 | Permission denied |
| 500 | Internal server error |

## Security

- **ApiKey**
