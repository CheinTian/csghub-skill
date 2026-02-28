# GET /accounting/subscriptions

**Resource:** [Accounting](../resources/Accounting.md)
**List subscriptions by user uuid and start time and end time**
**Operation ID:** `get--accounting-subscriptions`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `status` | query | string | Yes | status |
| `sku_type` | query | integer | Yes | sku_type |
| `start_time` | query | string | Yes | start_time, format: '2024-06-12 08:27:22' |
| `end_time` | query | string | Yes | end_time, format: '2024-06-12 17:17:22' |
| `user_uuid` | query | string | No | user uuid |
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
