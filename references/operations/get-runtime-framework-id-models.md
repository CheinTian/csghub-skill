# GET /runtime_framework/{id}/models

**Resource:** [RuntimeFramework](../resources/RuntimeFramework.md)
**Get Visible models by runtime framework for current user**
**Operation ID:** `get--runtime_framework-{id}-models`

get visible models by runtime framework for current user

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | runtime framework id |
| `current_user` | query | string | No | current user |
| `per` | query | integer | No | per |
| `page` | query | integer | No | per page |
| `deploy_type` | query | enum: 0, 1, 2 | No | deploy_type |

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
