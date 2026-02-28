# POST /agent/instances

**Resource:** [Agent](../resources/Agent.md)
**Create a new agent instance**
**Operation ID:** `post--agent-instances`

Create a new agent instance from a template. If data is provided, it is used to create the flow.

## Request Body

Agent instance data

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreateAgentInstanceRequest](../schemas/types-CreateAgentInstanceRequest/types-CreateAgentInstanceRequest.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
