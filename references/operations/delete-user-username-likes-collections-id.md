# DELETE /user/{username}/likes/collections/{id}

**Resource:** [User](../resources/User.md)
**delete collection likes**
**Operation ID:** `delete--user-{username}-likes-collections-{id}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `username` | path | string | Yes | username |
| `id` | path | string | Yes | collection id |

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
