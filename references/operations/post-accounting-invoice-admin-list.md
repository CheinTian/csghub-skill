# POST /accounting/invoice/admin/list

**Resource:** [Accounting-Invoices](../resources/Accounting-Invoices.md)
**List applicable invoices for the administrator**
**Operation ID:** `post--accounting-invoice-admin-list`

List all applicable invoices based on the request parameters provided by the administrator.

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `Authorization` | header | string | Yes | Authorization token (Bearer <token>) |

## Request Body

Invoice list request parameters

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.AccInvoiceListReq](../schemas/types-AccInvoiceListReq/types-AccInvoiceListReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | Applicable invoice list retrieved successfully |
| 400 | Bad request format |
| 500 | Server error |

**Success Response Schema:**

[types.AccInvoiceListResp](../schemas/types-AccInvoiceListResp/types-AccInvoiceListResp.md)

## Security

- **ApiKey**
