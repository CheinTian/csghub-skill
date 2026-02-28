# PUT /collections/{id}/repos/{repo_id}

**Resource:** [Collection](../resources/Collection.md)
**update repo remark**
**Operation ID:** `put--collections-{id}-repos-{repo_id}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | id |
| `repo_id` | path | string | Yes | repo_id |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UpdateCollectionRepoReq](../schemas/types-UpdateCollectionRepoReq/types-UpdateCollectionRepoReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **JWT token**
