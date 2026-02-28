# DELETE /{repo_type}/{namespace}/{name}/raw/{file_path}

**Resource:** [Repository](../resources/Repository.md)
**Delete existing file in repository**
**Operation ID:** `delete--{repo_type}-{namespace}-{name}-raw-{file_path}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `repo_type` | path | enum: models, datasets, codes... | Yes | models,datasets,codes,spaces or mcps |
| `namespace` | path | string | Yes | repo owner name |
| `name` | path | string | Yes | repo name |
| `file_path` | path | string | Yes | the file relative path |
| `current_user` | query | string | No | current user name |

## Request Body

delete file request

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.DeleteFileReq](../schemas/types-DeleteFileReq/types-DeleteFileReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
