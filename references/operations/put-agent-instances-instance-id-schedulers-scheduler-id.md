# PUT /agent/instances/{instance_id}/schedulers/{scheduler_id}

**Resource:** [Agent](../resources/Agent.md)
**Update agent scheduler**
**Operation ID:** `put--agent-instances-{instance_id}-schedulers-{scheduler_id}`

Update an existing agent scheduler (name, prompt, schedule, status, etc.). Scheduler must belong to the given instance.

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `instance_id` | path | integer | Yes | Agent instance ID |
| `scheduler_id` | path | integer | Yes | Scheduler ID |

## Request Body

Fields to update

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UpdateAgentSchedulerRequest](../schemas/types-UpdateAgentSchedulerRequest/types-UpdateAgentSchedulerRequest.md)

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
