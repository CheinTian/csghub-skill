# DELETE /models/{namespace}/{name}/finetune/{id}

**Resource:** [Model](../resources/Model.md)
**Delete a finetune instance**
**Operation ID:** `delete--models-{namespace}-{name}-finetune-{id}`

delete a finetune instance

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `id` | path | integer | Yes | id |
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
