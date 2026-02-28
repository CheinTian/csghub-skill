# POST /accounting/invoice/create

**Resource:** [Accounting-Invoices](../resources/Accounting-Invoices.md)
**Create a new invoice**
**Operation ID:** `post--accounting-invoice-create`

Create a new invoice based on the request parameters provided by the user. Before creation, check the bill date, invoice amount, etc.

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `Authorization` | header | string | Yes | Authorization token (Bearer <token>) |

## Request Body

Invoice creation request parameters

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.AccInvoiceCreateReq](../schemas/types-AccInvoiceCreateReq/types-AccInvoiceCreateReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | Invoice created successfully |
| 400 | Bad request format |
| 500 | Server error |

## Security

- **ApiKey**
