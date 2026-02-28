# GET /user/{username}/order/resources

**Resource:** [User](../resources/User.md)
**get user's resource**
**Operation ID:** `get--user-{username}-order-resources`

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
