# PUT /accounting/invoice/title/{id}

**Resource:** [Accounting-Invoices](../resources/Accounting-Invoices.md)
**Update invoice title**
**Operation ID:** `put--accounting-invoice-title-{id}`

Update the invoice title information for a user

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `Authorization` | header | string | Yes | Authorization token (Bearer <token>) |
| `id` | path | string | Yes | Invoice title ID |

## Request Body

Request body containing invoice title information

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.AccInvoiceTitleReq](../schemas/types-AccInvoiceTitleReq/types-AccInvoiceTitleReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
