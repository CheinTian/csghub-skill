# GET /accounting/present

**Resource:** [Accounting](../resources/Accounting.md)
**List non-cash recharges by user name, user uuid and time range**
**Operation ID:** `get--accounting-present`

List non-cash recharges (presents) by user name, user uuid and time range

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `user_name` | query | string | No | User name |
| `user_uuid` | query | string | No | User UUID |
| `start_date` | query | string | No | Start date, format: '2024-06-12' |
| `end_date` | query | string | No | End date, format: '2024-06-12' |
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
