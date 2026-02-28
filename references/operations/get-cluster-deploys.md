# GET /cluster/deploys

**Resource:** [Cluster](../resources/Cluster.md)
**Get cluster deploys**
**Operation ID:** `get--cluster-deploys`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `per` | query | integer | No | per |
| `page` | query | integer | No | page index |
| `status` | query | enum: all, running, stopped... | No | status |
| `search` | query | string | No | search |

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
