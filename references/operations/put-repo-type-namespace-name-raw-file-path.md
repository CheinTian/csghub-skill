# PUT /{repo_type}/{namespace}/{name}/raw/{file_path}

**Resource:** [Repository](../resources/Repository.md)
**Update existing file in repository**
**Operation ID:** `put--{repo_type}-{namespace}-{name}-raw-{file_path}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `repo_type` | path | enum: models, datasets, codes... | Yes | models,datasets,codes,spaces or mcps |
| `namespace` | path | string | Yes | repo owner name |
| `name` | path | string | Yes | repo name |
| `file_path` | path | string | Yes | the new file relative path |
| `current_user` | query | string | No | current user name |

## Request Body

create file request

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UpdateFileReq](../schemas/types-UpdateFileReq/types-UpdateFileReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
