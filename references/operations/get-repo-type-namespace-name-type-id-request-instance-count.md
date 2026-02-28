# GET /{repo_type}/{namespace}/{name}/{type}/{id}/request/{instance}/count

**Resource:** [Monitor](../resources/Monitor.md)
**Get instance request count**
**Operation ID:** `get--{repo_type}-{namespace}-{name}-{type}-{id}-request-{instance}-count`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `repo_type` | path | enum: models, spaces | Yes | models,spaces |
| `namespace` | path | string | Yes | repo owner name |
| `name` | path | string | Yes | repo name |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
