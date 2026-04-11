# GET /admin/cluster/workflows/time_range_report

**Resource:** [Cluster](../resources/Cluster.md)
**Get workflows by time range as CSV report**
**Operation ID:** `get--admin-cluster-workflows-time_range_report`

Get workflows by time range and return as CSV file download

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `start_time` | query | string | No | start time (e.g., 2024-01-01 or 2024-01-01 00:00:00) |
| `end_time` | query | string | No | end time (e.g., 2024-01-31 or 2024-01-31 23:59:59) |

## Responses

| Status | Description |
|--------|-------------|
| 200 | CSV file |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
