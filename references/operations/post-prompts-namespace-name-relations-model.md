# POST /prompts/{namespace}/{name}/relations/model

**Resource:** [Prompt](../resources/Prompt.md)
**add model relation for prompt, used for admin**
**Operation ID:** `post--prompts-{namespace}-{name}-relations-model`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `current_user` | query | string | No | current user |

## Request Body

add model relation

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.RelationModel](../schemas/types-RelationModel/types-RelationModel.md)

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
