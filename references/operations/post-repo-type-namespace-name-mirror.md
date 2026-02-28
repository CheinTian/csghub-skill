# POST /{repo_type}/{namespace}/{name}/mirror

**Resource:** [Repository](../resources/Repository.md)
**Create mirror for a existing repository**
**Operation ID:** `post--{repo_type}-{namespace}-{name}-mirror`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `repo_type` | path | enum: models, datasets, codes... | Yes | models,datasets,codes or spaces |
| `namespace` | path | string | Yes | repo owner name |
| `name` | path | string | Yes | repo name |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreateMirrorParams](../schemas/types-CreateMirrorParams/types-CreateMirrorParams.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
