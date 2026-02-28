# PUT /cluster/admin/nodes/{id}/vxpu/enable

**Resource:** [Cluster](../resources/Cluster.md)
**Enable cluster node**
**Operation ID:** `put--cluster-admin-nodes-{id}-vxpu-enable`

Enable a cluster node by its ID

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | Node ID |

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
