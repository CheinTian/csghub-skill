# GET /{repo_type}/{namespace}/{name}/run/{id}/status

**Resource:** [Repository](../resources/Repository.md)
**get deploy status**
**Operation ID:** `get--{repo_type}-{namespace}-{name}-run-{id}-status`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `repo_type` | path | enum: models, spaces | Yes | models,spaces |
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `id` | path | string | Yes | deploy id |
| `current_user` | query | string | Yes | current_user |

## Responses

| Status | Description |
|--------|-------------|
| 400 | Bad request |
| 401 | Permission denied |
| 500 | Internal server error |

## Security

- **JWT token**
