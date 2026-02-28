# POST /discussions/{id}/comments

**Resource:** [Discussion](../resources/Discussion.md)
**Create a new discussion comment**
**Operation ID:** `post--discussions-{id}-comments`

create a new discussion comment

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | the discussion id |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreateCommentRequest](../schemas/types-CreateCommentRequest/types-CreateCommentRequest.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
