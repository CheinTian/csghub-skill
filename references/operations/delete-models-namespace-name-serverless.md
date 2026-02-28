# DELETE /models/{namespace}/{name}/serverless

**Resource:** [Model](../resources/Model.md)
**remove a serverless service**
**Operation ID:** `delete--models-{namespace}-{name}-serverless`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `current_user` | query | string | Yes | current_user |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
