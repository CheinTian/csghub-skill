# GET /models

**Resource:** [Model](../resources/Model.md)
**Get Visiable models for current user**
**Operation ID:** `get--models`

get visiable models for current user

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `current_user` | query | string | No | current user |
| `search` | query | string | No | search text |
| `task_tag` | query | string | No | filter by task tag, deprecated |
| `framework_tag` | query | string | No | filter by framework tag, deprecated |
| `license_tag` | query | string | No | filter by license tag, deprecated |
| `language_tag` | query | string | No | filter by language tag, deprecated |
| `tag_category` | query | string | No | filter by tag category |
| `tag_name` | query | string | No | filter by tag name |
| `tag_group` | query | string | No | filter by tag group |
| `need_op_weight` | query | boolean | No | need op weight |
| `sort` | query | string | No | sort by |
| `source` | query | enum: opencsg, huggingface, local | No | source |
| `xnet_migration_status` | query | enum: pending, running, completed... | No | filter by xnet migration status |
| `per` | query | integer | No | per |
| `page` | query | integer | No | per page |
| `model_tree` | query | string | No | example: base_model:finetune:1 |
| `list_serverless` | query | boolean | No | list serverless |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
