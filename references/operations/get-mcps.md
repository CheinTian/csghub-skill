# GET /mcps

**Resource:** [MCP](../resources/MCP.md)
**Get Visiable mcp servers for current user**
**Operation ID:** `get--mcps`

Get visiable mcp servers for current user

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `current_user` | query | string | No | current user |
| `tag_category` | query | string | No | filter by tag category |
| `tag_name` | query | string | No | filter by tag name |
| `tag_group` | query | string | No | filter by tag group |
| `need_op_weight` | query | boolean | No | need op weight |
| `search` | query | string | No | search text |
| `sort` | query | string | No | sort by |
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
