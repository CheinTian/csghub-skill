# GET /{repo_type}/{namespace}/{name}/run/{id}/logs/{instance}

**Resource:** [Repository](../resources/Repository.md)
**get deploy instance logs**
**Operation ID:** `get--{repo_type}-{namespace}-{name}-run-{id}-logs-{instance}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `repo_type` | path | enum: models, spaces | Yes | models,spaces |
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `id` | path | string | Yes | id |
| `instance` | path | string | Yes | instance |
| `current_user` | query | string | Yes | current_user |
| `since` | query | string | No | since time. Optional values: 10mins, 30mins, 1hour, 6hours, 1day, 2days, 1week |

## Responses

| Status | Description |
|--------|-------------|
| 400 | Bad request |
| 401 | Permission denied |
| 500 | Internal server error |

## Security

- **ApiKey**
