# GET /skills

**Resource:** [Skill](../resources/Skill.md)
**Get Visiable skills for current user**
**Operation ID:** `get--skills`

get visiable skills for current user

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `current_user` | query | string | No | current user |
| `search` | query | string | No | search text |
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
