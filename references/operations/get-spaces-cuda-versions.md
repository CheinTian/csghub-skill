# GET /spaces/cuda-versions

**Resource:** [Space](../resources/Space.md)
**Get supported CUDA versions**
**Operation ID:** `get--spaces-cuda-versions`

Get supported CUDA versions for a space

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `resource_type` | query | string | Yes | resource_type |

## Responses

| Status | Description |
|--------|-------------|
| 200 | Success |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
