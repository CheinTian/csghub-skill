# DELETE /api/v1/storage/{bucket}/{key}

**Resource:** [StorageGateway](../resources/StorageGateway.md)
**Delete object from storage**
**Operation ID:** `delete--api-v1-storage-{bucket}-{key}`

Delete object from storage gateway

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

## Security

- **ApiKey**
