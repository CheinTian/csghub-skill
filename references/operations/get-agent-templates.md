# GET /agent/templates

**Resource:** [Agent](../resources/Agent.md)
**List agent templates for the current user**
**Operation ID:** `get--agent-templates`

Get all agent templates belonging to the current user

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `search` | query | string | No | search text |
| `type` | query | enum: langflow, code | No | type |
| `per` | query | integer | No | per |
| `page` | query | integer | No | per page |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 401 | Unauthorized |
| 500 | Internal server error |

## Security

- **ApiKey**
