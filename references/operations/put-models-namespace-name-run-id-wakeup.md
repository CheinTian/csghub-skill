# PUT /models/{namespace}/{name}/run/{id}/wakeup

**Resource:** [Model](../resources/Model.md)
**Wake up a model inference**
**Operation ID:** `put--models-{namespace}-{name}-run-{id}-wakeup`

Wake up  a model inference

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `id` | path | integer | Yes | deploy id |
| `current_user` | query | string | No | current user |

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
