# GET /cluster/admin/workflows

**Resource:** [Cluster](../resources/Cluster.md)
**Query cluster workflows**
**Operation ID:** `get--cluster-admin-workflows`

Query cluster workflows with filters

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `cluster_id` | query | string | No | cluster id |
| `cluster_node` | query | string | No | cluster node |
| `status` | query | string | No | status |
| `resource_id` | query | integer | No | resource id |
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
