# GET /internal/user/emails

**Resource:** [User](../resources/User.md)
**Get all user emails for internal services**
**Operation ID:** `get--internal-user-emails`

Retrieve all user email addresses for internal services

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `per` | query | integer | No | per |
| `page` | query | integer | No | per page |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
