# PUT /api/v1/storage/{bucket}/{key}

**Resource:** [StorageGateway](../resources/StorageGateway.md)
**Upload object to storage**
**Operation ID:** `put--api-v1-storage-{bucket}-{key}`

Upload object to storage gateway. If presigned URL parameters are present, the request is reverse proxied to OSS.

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `bucket` | path | string | Yes | Bucket name |
| `key` | path | string | Yes | Object key |

## Request Body

**Required:** Yes

**Content Types:** `multipart/form-data`

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
