# POST /agent/instances/{instance_id}/schedulers

**Resource:** [Agent](../resources/Agent.md)
**Create agent scheduler**
**Operation ID:** `post--agent-instances-{instance_id}-schedulers`

Create a new scheduled task for an agent instance. The scheduler runs the agent with the given prompt on the specified schedule (once, daily, weekly, monthly).

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `instance_id` | path | integer | Yes | Agent instance ID |

## Request Body

Scheduler configuration (instance_id in path takes precedence)

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreateAgentSchedulerRequest](../schemas/types-CreateAgentSchedulerRequest/types-CreateAgentSchedulerRequest.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 403 | Forbidden |
| 500 | Internal server error |

## Security

- **ApiKey**
