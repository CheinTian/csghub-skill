# GET /runtime_framework/{id}/architecture

**Resource:** [RuntimeFramework](../resources/RuntimeFramework.md)
**Get runtime framework architectures**
**Operation ID:** `get--runtime_framework-{id}-architecture`

get runtime framework architectures

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | runtime framework id |

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
