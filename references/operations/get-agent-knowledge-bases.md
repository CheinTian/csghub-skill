# GET /agent/knowledge-bases

**Resource:** [Agent](../resources/Agent.md)
**List agent knowledge bases**
**Operation ID:** `get--agent-knowledge-bases`

Get all agent knowledge bases for the current user with filtering and pagination

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `search` | query | string | No | Search term for name field |
| `public` | query | boolean | No | Filter by public status |
| `editable` | query | boolean | No | Filter by editable status (true = owned by user, false = not owned by user) |
| `per` | query | integer | No | Items per page |
| `page` | query | integer | No | Page number |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 401 | Unauthorized |
| 500 | Internal server error |

## Security

- **ApiKey**
