# GET /runtime_framework/models

**Resource:** [RuntimeFramework](../resources/RuntimeFramework.md)
**Get Visible models for all runtime frameworks for current user**
**Operation ID:** `get--runtime_framework-models`

get visible models for all runtime frameworks for current user

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `search` | query | string | No | search text |
| `sort` | query | string | No | sort by |
| `current_user` | query | string | No | current user |
| `per` | query | integer | No | per |
| `page` | query | integer | No | per page |
| `deploy_type` | query | enum: 1, 2 | No | deploy_type |

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
