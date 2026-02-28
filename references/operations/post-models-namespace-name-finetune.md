# POST /models/{namespace}/{name}/finetune

**Resource:** [Model](../resources/Model.md)
**create a finetune instance**
**Operation ID:** `post--models-{namespace}-{name}-finetune`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `current_user` | query | string | Yes | current_user |

## Request Body

deploy setting of instance

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.InstanceRunReq](../schemas/types-InstanceRunReq/types-InstanceRunReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
