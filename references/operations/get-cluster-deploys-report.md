# GET /cluster/deploys_report

**Resource:** [Cluster](../resources/Cluster.md)
**Export cluster deploys as CSV**
**Operation ID:** `get--cluster-deploys_report`

Export all cluster deploys (Excel-readable CSV) with streaming output

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `status` | query | enum: all, running, stopped... | No | status |
| `search` | query | string | No | search |
| `start_time` | query | string | No | filter deploys created after or at this time |
| `end_time` | query | string | No | filter deploys created before or at this time |

## Responses

| Status | Description |
|--------|-------------|
| 200 | CSV file |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
