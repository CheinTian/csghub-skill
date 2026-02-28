# GET /agent/tasks/{id}

**Resource:** [Agent](../resources/Agent.md)
**Get agent task detail**
**Operation ID:** `get--agent-tasks-{id}`

Get detailed information about a specific agent task

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | Task ID (primary key) |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 404 | Task not found |
| 500 | Internal server error |

## Security

- **ApiKey**
