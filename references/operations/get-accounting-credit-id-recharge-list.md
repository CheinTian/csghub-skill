# GET /accounting/credit/{id}/recharge/list

**Resource:** [Accounting](../resources/Accounting.md)
**List recharges by user uuid and start time and end time**
**Operation ID:** `get--accounting-credit-{id}-recharge-list`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | user uuid |
| `activity_id` | query | string | Yes | activity_id |
| `start_time` | query | string | Yes | start_time, format: '2024-06-12 08:27:22' |
| `end_time` | query | string | Yes | end_time, format: '2024-06-12 17:17:22' |
| `current_user` | query | string | Yes | current_user |
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
