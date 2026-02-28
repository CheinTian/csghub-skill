# POST /{repo_type}/{namespace}/{name}/commit/{revision}

**Resource:** [Repository](../resources/Repository.md)
**Create commit with batch files**
**Operation ID:** `post--{repo_type}-{namespace}-{name}-commit-{revision}`

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

**Schema:** [types.CommitFilesReq](../schemas/types-CommitFilesReq/types-CommitFilesReq.md)

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
