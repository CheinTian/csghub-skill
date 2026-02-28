# PUT /runtime_framework/{id}/architecture

**Resource:** [RuntimeFramework](../resources/RuntimeFramework.md)
**Set runtime framework architectures**
**Operation ID:** `put--runtime_framework-{id}-architecture`

set runtime framework architectures

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | runtime framework id |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.RuntimeArchitecture](../schemas/types-RuntimeArchitecture/types-RuntimeArchitecture.md)

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
