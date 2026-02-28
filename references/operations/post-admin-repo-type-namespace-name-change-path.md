# POST /admin/{repo_type}/{namespace}/{name}/change_path

**Resource:** [Repository](../resources/Repository.md)
**Change the namespace of a repository**
**Operation ID:** `post--admin-{repo_type}-{namespace}-{name}-change_path`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `repo_type` | path | enum: models | Yes | models |
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `current_user` | query | string | Yes | current_user |

## Request Body

deploy setting of inference

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.ChangePathReq](../schemas/types-ChangePathReq/types-ChangePathReq.md)

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
