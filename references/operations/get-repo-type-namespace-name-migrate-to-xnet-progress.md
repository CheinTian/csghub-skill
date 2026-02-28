# GET /{repo_type}/{namespace}/{name}/migrate_to_xnet_progress

**Resource:** [Repository](../resources/Repository.md)
**Migrate repo to Xnet progress**
**Operation ID:** `get--{repo_type}-{namespace}-{name}-migrate_to_xnet_progress`

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

## Security

- **ApiKey**
