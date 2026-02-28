# PUT /prompts/{namespace}/{name}

**Resource:** [Prompt](../resources/Prompt.md)
**Update a exists prompt repo**
**Operation ID:** `put--prompts-{namespace}-{name}`

update a exists prompt repo

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `current_user` | query | string | No | current user, the owner |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UpdatePromptRepoReq](../schemas/types-UpdatePromptRepoReq/types-UpdatePromptRepoReq.md)

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
