# POST /prompts

**Resource:** [Prompt](../resources/Prompt.md)
**Create a new prompt repo**
**Operation ID:** `post--prompts`

create a new prompt repo

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `current_user` | query | string | No | current user, the owner |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreatePromptRepoReq](../schemas/types-CreatePromptRepoReq/types-CreatePromptRepoReq.md)

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
