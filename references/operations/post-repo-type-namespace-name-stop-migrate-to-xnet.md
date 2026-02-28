# POST /{repo_type}/{namespace}/{name}/stop_migrate_to_xnet

**Resource:** [Repository](../resources/Repository.md)
**Stop single repo migration to Xnet**
**Operation ID:** `post--{repo_type}-{namespace}-{name}-stop_migrate_to_xnet`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `repo_type` | path | enum: models, datasets, codes... | Yes | models,datasets,codes or spaces |
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
