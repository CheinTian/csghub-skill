# POST /{repo_type}/{namespace}/{name}/discussions

**Resource:** [Discussion](../resources/Discussion.md)
**Create a new repo discussion**
**Operation ID:** `post--{repo_type}-{namespace}-{name}-discussions`

create a new repo discussion

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `current_user` | query | string | Yes | current user, the owner |
| `repo_type` | path | enum: models, datasets, codes... | Yes | repository type |
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreateRepoDiscussionRequest](../schemas/types-CreateRepoDiscussionRequest/types-CreateRepoDiscussionRequest.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
