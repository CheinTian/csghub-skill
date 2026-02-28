# POST /accounting/invoice/dashboard

**Resource:** [Accounting-Invoices](../resources/Accounting-Invoices.md)
**Get invoice dashboard data**
**Operation ID:** `post--accounting-invoice-dashboard`

Get invoice dashboard data, including non-invoiceable amount, invoiced amount, and uninvoiced amount for the current month, based on the time range and user ID provided by the user.

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `Authorization` | header | string | Yes | Authorization token (Bearer <token>) |

## Request Body

Invoice Dashboard request parameters

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.AccInvoiceDashboardReq](../schemas/types-AccInvoiceDashboardReq/types-AccInvoiceDashboardReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | Invoice dashboard data retrieved successfully |
| 400 | Bad request format |
| 500 | Server error |

**Success Response Schema:**

[types.AccInvoiceDashboardResp](../schemas/types-AccInvoiceDashboardResp/types-AccInvoiceDashboardResp.md)

## Security

- **ApiKey**
