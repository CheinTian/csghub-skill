# PUT /accounting/invoice/admin/{id}

**Resource:** [Accounting-Invoices](../resources/Accounting-Invoices.md)
**Update invoice information (admin)**
**Operation ID:** `put--accounting-invoice-admin-{id}`

The administrator updates the invoice information with the specified ID. Invoice status eq issued,failed

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `Authorization` | header | string | Yes | Authorization token (Bearer <token>) |
| `id` | path | integer | Yes | Invoice ID |

## Request Body

Update request parameters

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.AdminUpdateInvoiceReq](../schemas/types-AdminUpdateInvoiceReq/types-AdminUpdateInvoiceReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | Successfully return the updated invoice information |
| 400 | Bad request format |
| 500 | Server error |

**Success Response Schema:**

[types.AccInvoiceResp](../schemas/types-AccInvoiceResp/types-AccInvoiceResp.md)

