# POST /{repo_type}/{namespace}/{name}/mirror_from_saas

**Resource:** [Repository](../resources/Repository.md)
**Mirror repo from OpenCSG Saas(only on-premises)**
**Operation ID:** `post--{repo_type}-{namespace}-{name}-mirror_from_saas`

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
