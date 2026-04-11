# GET /organization/{namespace}/run/{repo_type}

**Resource:** [Organization](../resources/Organization.md)
**Get organization run deploys (e.g. inference)**
**Operation ID:** `get--organization-{namespace}-run-{repo_type}`

get organization run deploys by deploy type (0-space, 1-inference, 2-finetune)

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | org name |
| `repo_type` | path | enum: model, space | Yes | model or space |
| `deploy_type` | query | integer | No | deploy type (0-space, 1-inference, 2-finetune) |
| `per` | query | integer | No | page size |
| `page` | query | integer | No | current page number |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
