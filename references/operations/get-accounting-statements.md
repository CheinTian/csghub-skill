# GET /accounting/statements

**Resource:** [Accounting](../resources/Accounting.md)
**List statements by user name, instance name, scene and time range**
**Operation ID:** `get--accounting-statements`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `user_name` | query | string | No | User name |
| `instance_name` | query | string | No | Instance name |
| `scene` | query | integer | No | Scene |
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

[types.Response](../schemas/types-Response/types-Response.md)

## Security

- **ApiKey**
