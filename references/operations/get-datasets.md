# GET /datasets

**Resource:** [Dataset](../resources/Dataset.md)
**Get Visiable datasets for current user**
**Operation ID:** `get--datasets`

get visiable datasets for current user

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `current_user` | query | string | No | current user |
| `search` | query | string | No | search text |
| `task_tag` | query | string | No | filter by task tag |
| `framework_tag` | query | string | No | filter by framework tag |
| `license_tag` | query | string | No | filter by license tag |
| `language_tag` | query | string | No | filter by language tag |
| `sort` | query | string | No | sort by |
| `source` | query | enum: opencsg, huggingface, local | No | source |
| `xnet_migration_status` | query | enum: pending, running, completed... | No | filter by xnet migration status |
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
