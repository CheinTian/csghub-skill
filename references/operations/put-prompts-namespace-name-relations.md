# PUT /prompts/{namespace}/{name}/relations

**Resource:** [Prompt](../resources/Prompt.md)
**Set model relation for prompt**
**Operation ID:** `put--prompts-{namespace}-{name}-relations`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `current_user` | query | string | No | current user |

## Request Body

set model relation

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.RelationModels](../schemas/types-RelationModels/types-RelationModels.md)

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
