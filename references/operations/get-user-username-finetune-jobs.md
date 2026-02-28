# GET /user/{username}/finetune/jobs

**Resource:** [User](../resources/User.md)
**Get user backend fintunes**
**Operation ID:** `get--user-{username}-finetune-jobs`

get user backend fintunes

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
