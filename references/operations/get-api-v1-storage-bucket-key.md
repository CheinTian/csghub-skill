# GET /api/v1/storage/{bucket}/{key}

**Resource:** [StorageGateway](../resources/StorageGateway.md)
**Get object from storage**
**Operation ID:** `get--api-v1-storage-{bucket}-{key}`

Get object using proxy mode. If presigned URL parameters are present, reverse proxy to OSS. Otherwise, use S3 client to fetch object.

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `bucket` | path | string | Yes | Bucket name |
| `key` | path | string | Yes | Object key |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK (streams object) |
| 400 | Bad request |
| 404 | Object not found |
| 500 | Internal server error |

**Success Response Schema:**

[types.Response](../schemas/types-Response/types-Response.md)

## Security

- **ApiKey**
