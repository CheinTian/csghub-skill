# DELETE /models/{namespace}/{name}/run/versions/{id}/{commit_id}

**Resource:** [Model](../resources/Model.md)
**delete inference version**
**Operation ID:** `delete--models-{namespace}-{name}-run-versions-{id}-{commit_id}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `id` | path | integer | Yes | id |
| `commit_id` | path | string | Yes | commit_id |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

**Success Response Schema:**

[types.Response](../schemas/types-Response/types-Response.md)

## Security

- **ApiKey**
