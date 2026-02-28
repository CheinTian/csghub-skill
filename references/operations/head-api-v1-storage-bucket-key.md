# HEAD /api/v1/storage/{bucket}/{key}

**Resource:** [StorageGateway](../resources/StorageGateway.md)
**Get object metadata**
**Operation ID:** `head--api-v1-storage-{bucket}-{key}`

Get object metadata without downloading the object

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `bucket` | path | string | Yes | Bucket name |
| `key` | path | string | Yes | Object key |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 404 | Not found |
| 500 | Internal server error |

**Success Response Schema:**

[types.Response](../schemas/types-Response/types-Response.md)

## Security

- **ApiKey**
