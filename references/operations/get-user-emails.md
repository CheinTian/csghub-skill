# GET /user/emails

**Resource:** [User](../resources/User.md)
**Get all user emails**
**Operation ID:** `get--user-emails`

Retrieve all user email addresses

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
