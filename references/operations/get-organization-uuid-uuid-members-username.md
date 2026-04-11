# GET /organization/uuid/{uuid}/members/{username}

**Resource:** [Member](../resources/Member.md)
**Get user's role in an org by uuid and username**
**Operation ID:** `get--organization-uuid-{uuid}-members-{username}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `uuid` | path | string | Yes | org uuid |
| `username` | path | string | Yes | user name |
| `current_user` | query | string | No | the op user |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
