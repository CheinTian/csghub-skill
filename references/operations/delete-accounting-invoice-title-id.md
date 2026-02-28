# DELETE /accounting/invoice/title/{id}

**Resource:** [Accounting-Invoices](../resources/Accounting-Invoices.md)
**Delete invoice title.**
**Operation ID:** `delete--accounting-invoice-title-{id}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `Authorization` | header | string | Yes | Authorization token (Bearer <token>) |
| `id` | path | string | Yes | Invoice title ID |

## Responses

| Status | Description |
|--------|-------------|
| 200 | Delete successful |
| 400 | Bad request format |
| 500 | Server error |

## Security

- **ApiKey**
