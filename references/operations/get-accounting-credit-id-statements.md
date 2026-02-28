# GET /accounting/credit/{id}/statements

**Resource:** [Accounting](../resources/Accounting.md)
**List statements by user uuid and start time and end time**
**Operation ID:** `get--accounting-credit-{id}-statements`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | user uuid |
| `scene` | query | enum: 10, 11, 12... | No | scene |
| `instance_name` | query | string | Yes | instance name |
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
