# GET /models/runtime_framework

**Resource:** [Repository](../resources/Repository.md)
**List repo runtime framework**
**Operation ID:** `get--models-runtime_framework`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `repo_type` | path | enum: models | Yes | models |
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `current_user` | query | string | No | current user |
| `deploy_type` | query | enum: 0, 1, 2 | No | deploy_type |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
