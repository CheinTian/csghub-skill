# POST /models/{namespace}/{name}/relations/dataset

**Resource:** [Model](../resources/Model.md)
**add dataset relation for model**
**Operation ID:** `post--models-{namespace}-{name}-relations-dataset`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `current_user` | query | string | No | current user |

## Request Body

add dataset relation

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.RelationDataset](../schemas/types-RelationDataset/types-RelationDataset.md)

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
