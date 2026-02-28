# GET /accounting/stripe/pay/sessions/{id}

**Resource:** [Accounting](../resources/Accounting.md)
**Get a stripe pay session**
**Operation ID:** `get--accounting-stripe-pay-sessions-{id}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | id |

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
