# GET /codes

**Resource:** [Code](../resources/Code.md)
**Get Visiable codes for current user**
**Operation ID:** `get--codes`

get visiable codes for current user

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `current_user` | query | string | No | current user |
| `search` | query | string | No | search text |
| `task_tag` | query | string | No | filter by task tag |
| `framework_tag` | query | string | No | filter by framework tag |
| `license_tag` | query | string | No | filter by license tag |
| `language_tag` | query | string | No | filter by language tag |
| `need_op_weight` | query | boolean | No | need op weight |
| `sort` | query | string | No | sort by |
| `source` | query | enum: opencsg, huggingface, local | No | source |
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
