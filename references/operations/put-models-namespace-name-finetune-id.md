# PUT /models/{namespace}/{name}/finetune/{id}

**Resource:** [Model](../resources/Model.md)
**Update a finetune instance**
**Operation ID:** `put--models-{namespace}-{name}-finetune-{id}`

update finetune instance resource_id and cluster_id (deploy must be stopped first)

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `id` | path | integer | Yes | finetune deploy id |

## Request Body

at least resource_id to update resource and cluster

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
