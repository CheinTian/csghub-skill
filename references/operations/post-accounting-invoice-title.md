# POST /accounting/invoice/title

**Resource:** [Accounting-Invoices](../resources/Accounting-Invoices.md)
**Create a new invoice title.**
**Operation ID:** `post--accounting-invoice-title`

Creates a new invoice title.

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `Authorization` | header | string | Yes | Authorization token (Bearer <token>) |

## Request Body

Invoice title information

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.AccInvoiceTitleReq](../schemas/types-AccInvoiceTitleReq/types-AccInvoiceTitleReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | Creation successful |
| 400 | Bad request format |
| 500 | Server error |

**Success Response Schema:**

[types.AccInvoiceTitleResp](../schemas/types-AccInvoiceTitleResp/types-AccInvoiceTitleResp.md)

## Security

- **ApiKey**
