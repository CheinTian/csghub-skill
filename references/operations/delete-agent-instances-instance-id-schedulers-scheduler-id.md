# DELETE /agent/instances/{instance_id}/schedulers/{scheduler_id}

**Resource:** [Agent](../resources/Agent.md)
**Delete agent scheduler**
**Operation ID:** `delete--agent-instances-{instance_id}-schedulers-{scheduler_id}`

Delete an agent scheduler and cancel its schedule. Scheduler must belong to the given instance.

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `instance_id` | path | integer | Yes | Agent instance ID |
| `scheduler_id` | path | integer | Yes | Scheduler ID |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 403 | Forbidden |
| 404 | Not found |
| 500 | Internal server error |

**Success Response Schema:**

[types.Response](../schemas/types-Response/types-Response.md)

## Security

- **ApiKey**
