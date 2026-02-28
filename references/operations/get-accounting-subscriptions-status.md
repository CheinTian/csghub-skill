# GET /accounting/subscriptions/status

**Resource:** [Accounting](../resources/Accounting.md)
**Get user subscription status**
**Operation ID:** `get--accounting-subscriptions-status`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `sku_type` | query | string | Yes | sku_type |

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
