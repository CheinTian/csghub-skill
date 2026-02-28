# DELETE /accounting/invoice/admin/{id}

**Resource:** [Accounting-Invoices](../resources/Accounting-Invoices.md)
**Delete an invoice by admin**
**Operation ID:** `delete--accounting-invoice-admin-{id}`

Delete an invoice by admin based on the provided invoice ID.

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `Authorization` | header | string | Yes | Authorization token (Bearer <token>) |
| `id` | path | string | Yes | Invoice ID |

## Responses

| Status | Description |
|--------|-------------|
| 200 | Delete successful |
| 400 | Bad request format |
| 500 | Server error |

## Security

- **ApiKey**
