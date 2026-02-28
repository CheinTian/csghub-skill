# POST /accounting/invoice/invoicable

**Resource:** [Accounting-Invoices](../resources/Accounting-Invoices.md)
**Get the list of invoicable items**
**Operation ID:** `post--accounting-invoice-invoicable`

Get the list of invoicable items based on the user's UUID and time range.

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `Authorization` | header | string | Yes | Authorization token (Bearer <token>) |

## Request Body

Invoicable request parameters

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.AccInvoicableReq](../schemas/types-AccInvoicableReq/types-AccInvoicableReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | Invoicable list retrieved successfully |
| 400 | Bad request format |
| 500 | Server error |

**Success Response Schema:**

[types.AccInvoicableResp](../schemas/types-AccInvoicableResp/types-AccInvoicableResp.md)

## Security

- **ApiKey**
