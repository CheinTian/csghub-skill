# GET /accounting/credit/{id}/bills/instance

**Resource:** [Accounting](../resources/Accounting.md)
**List user bills detail by user uuid, instance name, start date and end date**
**Operation ID:** `get--accounting-credit-{id}-bills-instance`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | user uuid |
| `instance_name` | path | string | Yes | instance name |
| `scene` | query | enum: 10, 11, 12... | No | scene |
| `start_date` | query | string | Yes | start_date, format: '2024-06-12' |
| `end_date` | query | string | Yes | end_date, format: '2024-07-12' |
| `instance_name` | query | string | Yes | instance name |
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
