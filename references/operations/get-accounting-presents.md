# GET /accounting/presents

**Resource:** [Accounting](../resources/Accounting.md)
**List non-cash recharges by user UUID, time range and pagination**
**Operation ID:** `get--accounting-presents`

List non-cash recharges (presents) by user UUID, time range and pagination

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
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

[types.PresentsIndexResp](../schemas/types-PresentsIndexResp/types-PresentsIndexResp.md)

## Security

- **ApiKey**
