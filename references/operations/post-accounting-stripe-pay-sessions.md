# POST /accounting/stripe/pay/sessions

**Resource:** [Accounting](../resources/Accounting.md)
**Create stripe pay session**
**Operation ID:** `post--accounting-stripe-pay-sessions`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `current_user` | query | string | Yes | current_user |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreateStripeSessionReq](../schemas/types-CreateStripeSessionReq/types-CreateStripeSessionReq.md)

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
