# GET /mcps/tools

**Resource:** [MCP](../resources/MCP.md)
**Get Visiable mcp servers tools for current user**
**Operation ID:** `get--mcps-tools`

Get visiable mcp servers tools for current user

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `search` | query | string | No | search text |
| `per` | query | integer | No | per |
| `page` | query | integer | No | per page |
| `current_user` | query | string | No | current user |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
