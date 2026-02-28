# PUT /models/{namespace}/{name}/relations

**Resource:** [Model](../resources/Model.md)
**Set dataset relation for model**
**Operation ID:** `put--models-{namespace}-{name}-relations`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `current_user` | query | string | No | current user |

## Request Body

set dataset relation

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.RelationDatasets](../schemas/types-RelationDatasets/types-RelationDatasets.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
