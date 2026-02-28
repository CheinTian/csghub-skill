# POST /prompts/{namespace}/{name}/tags/{category}

**Resource:** [Prompt](../resources/Prompt.md)
**update the tags of a certain category**
**Operation ID:** `post--prompts-{namespace}-{name}-tags-{category}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | repo owner name |
| `name` | path | string | Yes | repo name |
| `current_user` | query | string | Yes | current user name |
| `category` | path | enum: task, license, framework... | Yes | tag category |

## Request Body

tag names in array

**Required:** Yes

**Content Types:** `application/json`

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
