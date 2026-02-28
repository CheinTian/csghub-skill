# PUT /cluster/admin/nodes/{id}/{namespace}/set_access_mode

**Resource:** [Cluster](../resources/Cluster.md)
**Set node access mode**
**Operation ID:** `put--cluster-admin-nodes-{id}-{namespace}-set_access_mode`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | Node ID |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.SetNodeAccessModeReq](../schemas/types-SetNodeAccessModeReq/types-SetNodeAccessModeReq.md)

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
