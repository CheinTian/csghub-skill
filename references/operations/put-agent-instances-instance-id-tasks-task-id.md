# PUT /agent/instances/{instance_id}/tasks/{task_id}

**Resource:** [Agent](../resources/Agent.md)
**Update scheduler task status**
**Operation ID:** `put--agent-instances-{instance_id}-tasks-{task_id}`

Update a scheduler task's status, name, error_message, and/or session_uuid in the database. Task must belong to the given instance and current user.

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `instance_id` | path | integer | Yes | Agent instance ID |
| `task_id` | path | integer | Yes | Task ID |

## Request Body

Status (required), optional name, error_message, and session_uuid

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UpdateAgentSchedulerTaskRequest](../schemas/types-UpdateAgentSchedulerTaskRequest/types-UpdateAgentSchedulerTaskRequest.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 403 | Forbidden |
| 404 | Not found |
| 500 | Internal server error |

## Security

- **ApiKey**
