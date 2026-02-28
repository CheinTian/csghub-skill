# GET /user/{username}/evaluations

**Resource:** [User](../resources/User.md)
**Get user evaluations**
**Operation ID:** `get--user-{username}-evaluations`

get user evaluations

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `username` | path | string | Yes | username |
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
