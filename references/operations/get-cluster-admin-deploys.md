# GET /cluster/admin/deploys

**Resource:** [Cluster](../resources/Cluster.md)
**Query cluster deploys**
**Operation ID:** `get--cluster-admin-deploys`

Query cluster deploys with filters

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `cluster_id` | query | string | No | cluster id |
| `cluster_node` | query | string | No | cluster node |
| `status` | query | integer | No | status |
| `resource_id` | query | string | No | resource id |
| `search` | query | string | No | search keyword |
| `per` | query | integer | No | per page |
| `page` | query | integer | No | page |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
