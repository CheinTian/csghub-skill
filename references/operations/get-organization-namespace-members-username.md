# GET /organization/{namespace}/members/{username}

**Resource:** [Member](../resources/Member.md)
**Get user's role in an org**
**Operation ID:** `get--organization-{namespace}-members-{username}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | org name |
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
