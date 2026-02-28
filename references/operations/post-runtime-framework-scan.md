# POST /runtime_framework/scan

**Resource:** [Model](../resources/Model.md)
**Scan model metadata**
**Operation ID:** `post--runtime_framework-scan`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `scan_type` | query | enum: 0, 1 | No | scan_type(0:all models, 1:new models) |

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
