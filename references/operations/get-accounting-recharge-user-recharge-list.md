# GET /accounting/recharge/user-recharge-list

**Resource:** [Accounting](../resources/Accounting.md)
**List current user recharge list by start_time and end_time and query**
**Operation ID:** `get--accounting-recharge-user-recharge-list`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `recharge_status` | query | string | No | Recharge status, options: 'succeed, waitpay' |
| `recharge_payment_type` | query | string | No | Recharge payment type, options: 'wx_pub_qr, alipay_qr' |
| `query` | query | string | No | Query string against recharge uuid |
| `start_time` | query | string | Yes | Start time, format: '2024-06-12 08:27:22' |
| `end_time` | query | string | Yes | End time, format: '2024-06-12 17:17:22' |
| `current_user` | query | string | Yes | Current user identifier |
| `per` | query | integer | No | Items per page |
| `page` | query | integer | No | Page number |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

**Success Response Schema:**

[types.Response](../schemas/types-Response/types-Response.md)

## Security

- **ApiKey**
