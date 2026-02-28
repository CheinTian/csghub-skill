# PUT /{repo_type}/{namespace}/{name}/incr_downloads

**Resource:** [Repository](../resources/Repository.md)
**Increase repo download count by 1**
**Operation ID:** `put--{repo_type}-{namespace}-{name}-incr_downloads`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `repo_type` | path | enum: models, datasets, codes... | Yes | models,dataset,codes or spaces |
| `namespace` | path | string | Yes | repo owner name |
| `name` | path | string | Yes | repo name |

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
