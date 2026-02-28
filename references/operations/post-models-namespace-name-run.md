# POST /models/{namespace}/{name}/run

**Resource:** [Model](../resources/Model.md)
**run model as inference**
**Operation ID:** `post--models-{namespace}-{name}-run`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `current_user` | query | string | Yes | current_user |

## Request Body

deploy setting of inference

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.ModelRunReq](../schemas/types-ModelRunReq/types-ModelRunReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
