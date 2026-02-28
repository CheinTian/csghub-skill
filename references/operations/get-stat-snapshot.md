# GET /stat/snapshot

**Resource:** [Stat](../resources/Stat.md)
**Get stat snapshot**
**Operation ID:** `get--stat-snapshot`

Retrieve statistical snapshot for a given target and date type

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `target_type` | query | string | Yes | Target type |
| `date_type` | query | enum: year, month, week... | Yes | Date type |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
