# GET /accounting/invoice/admin/{id}

**Resource:** [Accounting-Invoices](../resources/Accounting-Invoices.md)
**Get an invoice by ID for administrators.(only admin)**
**Operation ID:** `get--accounting-invoice-admin-{id}`

Get an invoice by ID for administrators.

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `Authorization` | header | string | Yes | Authorization token (Bearer <token>) |
| `id` | path | string | Yes | Invoice ID |

## Responses

| Status | Description |
|--------|-------------|
| 200 | Get invoice successful |
| 400 | Bad request format |
| 500 | Server error |

**Success Response Schema:**

[types.AccInvoiceResp](../schemas/types-AccInvoiceResp/types-AccInvoiceResp.md)

## Security

- **ApiKey**
