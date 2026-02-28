# GET /runtime_framework

**Resource:** [RuntimeFramework](../resources/RuntimeFramework.md)
**Get all runtime frameworks for current user**
**Operation ID:** `get--runtime_framework`

get all runtime frameworks for current user

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `current_user` | query | string | No | current user |
| `deploy_type` | query | enum: 1, 2, 3... | No | deploy_type |

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
