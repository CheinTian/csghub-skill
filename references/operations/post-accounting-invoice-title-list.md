# POST /accounting/invoice/title/list

**Resource:** [Accounting-Invoices](../resources/Accounting-Invoices.md)
**List all invoice titles**
**Operation ID:** `post--accounting-invoice-title-list`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `Authorization` | header | string | Yes | Authorization token (Bearer <token>) |

## Request Body

Invoice title list request

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.AccInvoiceTitleListReq](../schemas/types-AccInvoiceTitleListReq/types-AccInvoiceTitleListReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | List successful |
| 400 | Bad request format |
| 500 | Server error |

**Success Response Schema:**

[types.AccInvoiceTitleListResp](../schemas/types-AccInvoiceTitleListResp/types-AccInvoiceTitleListResp.md)

## Security

- **ApiKey**
