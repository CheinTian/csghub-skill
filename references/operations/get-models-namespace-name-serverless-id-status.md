# GET /models/{namespace}/{name}/serverless/{id}/status

**Resource:** [Model](../resources/Model.md)
**get serverless status**
**Operation ID:** `get--models-{namespace}-{name}-serverless-{id}-status`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `id` | path | string | Yes | deploy id |
| `current_user` | query | string | Yes | current_user |

## Responses

| Status | Description |
|--------|-------------|
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **JWT token**
