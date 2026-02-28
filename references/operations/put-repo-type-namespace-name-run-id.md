# PUT /{repo_type}/{namespace}/{name}/run/{id}

**Resource:** [Repository](../resources/Repository.md)
**Update deploy parameters**
**Operation ID:** `put--{repo_type}-{namespace}-{name}-run-{id}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `repo_type` | path | enum: models | Yes | models |
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `id` | path | string | Yes | deploy id |
| `current_user` | query | string | Yes | current_user |

## Request Body

deploy setting of inference

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.DeployUpdateReq](../schemas/types-DeployUpdateReq/types-DeployUpdateReq.md)

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
