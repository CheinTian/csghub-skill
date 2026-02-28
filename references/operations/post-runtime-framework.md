# POST /runtime_framework

**Resource:** [RuntimeFramework](../resources/RuntimeFramework.md)
**Create runtime framework**
**Operation ID:** `post--runtime_framework`

create runtime framework

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `repo_type` | path | enum: models, spaces | Yes | models,spaces |
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `current_user` | query | string | No | current user |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.RuntimeFrameworkReq](../schemas/types-RuntimeFrameworkReq/types-RuntimeFrameworkReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

**Success Response Schema:**

[types.RuntimeFramework](../schemas/types-RuntimeFramework/types-RuntimeFramework.md)

## Security

- **ApiKey**
