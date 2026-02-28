# GET /models/{namespace}/{name}/run/versions/{id}

**Resource:** [Model](../resources/Model.md)
**list all inference versions**
**Operation ID:** `get--models-{namespace}-{name}-run-versions-{id}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `id` | path | integer | Yes | id |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
