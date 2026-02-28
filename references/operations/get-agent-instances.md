# GET /agent/instances

**Resource:** [Agent](../resources/Agent.md)
**List agent instances for the current user**
**Operation ID:** `get--agent-instances`

Get all agent instances belonging to the current user

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `search` | query | string | No | search text |
| `type` | query | enum: langflow, code | No | type |
| `built_in` | query | boolean | No | built in |
| `public` | query | boolean | No | public |
| `editable` | query | boolean | No | editable |
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
