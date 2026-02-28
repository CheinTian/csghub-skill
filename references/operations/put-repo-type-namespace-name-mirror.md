# PUT /{repo_type}/{namespace}/{name}/mirror

**Resource:** [Repository](../resources/Repository.md)
**Update a mirror for a existing repository**
**Operation ID:** `put--{repo_type}-{namespace}-{name}-mirror`

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

**Schema:** [types.UpdateMirrorParams](../schemas/types-UpdateMirrorParams/types-UpdateMirrorParams.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
