# PUT /discussions/{id}

**Resource:** [Discussion](../resources/Discussion.md)
**Update a discussion**
**Operation ID:** `put--discussions-{id}`

update a discussion

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | the discussion id |
| `current_user` | query | string | Yes | current user, the owner |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UpdateDiscussionRequest](../schemas/types-UpdateDiscussionRequest/types-UpdateDiscussionRequest.md)

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
