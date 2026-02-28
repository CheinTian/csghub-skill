# POST /{repo_type}/{namespace}/{name}/preupload/{revision}

**Resource:** [Repository](../resources/Repository.md)
**Get upload mode for files**
**Operation ID:** `post--{repo_type}-{namespace}-{name}-preupload-{revision}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `repo_type` | path | enum: models, datasets, codes... | Yes | models,datasets,codes or spaces |
| `namespace` | path | string | Yes | repo owner name |
| `name` | path | string | Yes | repo name |
| `revision` | path | string | Yes | revision |
| `current_user` | query | string | No | current user name |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.PreuploadReq](../schemas/types-PreuploadReq/types-PreuploadReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
