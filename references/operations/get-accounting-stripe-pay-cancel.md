# GET /accounting/stripe/pay/cancel

**Resource:** [Accounting](../resources/Accounting.md)
**Mark stripe pay session as cancel**
**Operation ID:** `get--accounting-stripe-pay-cancel`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `session_id` | query | string | Yes | session_id |

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
