# GET /cluster/admin/nodes/{id}

**Resource:** [Cluster](../resources/Cluster.md)
**Get cluster node by ID**
**Operation ID:** `get--cluster-admin-nodes-{id}`

Get a single cluster node by its ID with region information

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
