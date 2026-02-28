# GET /accounting/recharge/list

**Resource:** [Accounting](../resources/Accounting.md)
**List recharges by user name, order no, status, payment type and time range**
**Operation ID:** `get--accounting-recharge-list`

List recharges by user name, order no, recharge status, payment type and time range

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `user_uuid` | query | string | Yes | user uuid |
| `order_no` | query | string | No | Order number |
| `recharge_status` | query | string | No | Recharge status |
| `recharge_payment_type` | query | string | No | Recharge payment type |
| `start_date` | query | string | Yes | Start date, format: '2024-06-12' |
| `end_date` | query | string | Yes | End date, format: '2024-06-12' |
| `per` | query | integer | No | Items per page |
| `page` | query | integer | No | Page number |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

**Success Response Schema:**

[types.RechargesIndexResp](../schemas/types-RechargesIndexResp/types-RechargesIndexResp.md)

## Security

- **ApiKey**
