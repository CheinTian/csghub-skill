# GET /user/{username}/run/serverless

**Resource:** [User](../resources/User.md)
**Get serverless deploys**
**Operation ID:** `get--user-{username}-run-serverless`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `username` | path | string | Yes | username |
| `per` | query | integer | No | per |
| `page` | query | integer | No | page index |
| `current_user` | query | string | No | current user |
| `search` | query | string | No | search by path or deployname |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
