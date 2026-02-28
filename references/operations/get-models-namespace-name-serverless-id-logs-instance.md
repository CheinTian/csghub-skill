# GET /models/{namespace}/{name}/serverless/{id}/logs/{instance}

**Resource:** [Model](../resources/Model.md)
**get serverless logs**
**Operation ID:** `get--models-{namespace}-{name}-serverless-{id}-logs-{instance}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `repo_type` | path | enum: models | Yes | models |
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `id` | path | string | Yes | id |
| `instance` | path | string | Yes | instance |
| `current_user` | query | string | Yes | current_user |
| `since` | query | string | No | since time. Optional values: 10mins, 30mins, 1hour, 6hours, 1day, 2days, 1week |

## Responses

| Status | Description |
|--------|-------------|
| 400 | Bad request. May occur when the since time format is unsupported |
| 500 | Internal server error |

## Security

- **ApiKey**
