# GET /user/{username}/run/{repo_type}

**Resource:** [User](../resources/User.md)
**Get user running deploys**
**Operation ID:** `get--user-{username}-run-{repo_type}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `username` | path | string | Yes | username |
| `repo_type` | path | enum: model, space | Yes | model,space |
| `deploy_type` | query | enum: 0, 1, 2 | No | deploy type(0-space,1-inference,2-finetune) |
| `per` | query | integer | No | per |
| `page` | query | integer | No | page index |
| `current_user` | query | string | No | current user |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
