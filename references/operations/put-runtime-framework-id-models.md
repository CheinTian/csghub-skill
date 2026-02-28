# PUT /runtime_framework/{id}/models

**Resource:** [RuntimeFramework](../resources/RuntimeFramework.md)
**Set model runtime frameworks**
**Operation ID:** `put--runtime_framework-{id}-models`

set model runtime frameworks

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | runtime framework id |
| `deploy_type` | query | enum: 0, 1, 2 | No | deploy_type |
| `current_user` | query | string | No | current user |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.RuntimeFrameworkModels](../schemas/types-RuntimeFrameworkModels/types-RuntimeFrameworkModels.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 403 | Forbidden |
| 500 | Internal server error |

**Success Response Schema:**

[types.Response](../schemas/types-Response/types-Response.md)

## Security

- **ApiKey**
