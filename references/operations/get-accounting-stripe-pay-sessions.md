# GET /accounting/stripe/pay/sessions

**Resource:** [Accounting](../resources/Accounting.md)
**List pay sessions by user uuid and start time and end time**
**Operation ID:** `get--accounting-stripe-pay-sessions`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `start_time` | query | string | Yes | start_time, format: '2024-06-12 08:27:22' |
| `end_time` | query | string | Yes | end_time, format: '2024-06-12 17:17:22' |
| `user_uuid` | query | string | Yes | user uuid |
| `session_status` | query | string | Yes | session status |
| `per` | query | integer | No | per |
| `page` | query | integer | No | per page |

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
