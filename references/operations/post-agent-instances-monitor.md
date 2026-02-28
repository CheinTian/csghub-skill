# POST /agent/instances/monitor

**Resource:** [Agent](../resources/Agent.md)
**Monitor status for agent instances**
**Operation ID:** `post--agent-instances-monitor`

## Request Body

Agent monitor request

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.AgentMonitorRequest](../schemas/types-AgentMonitorRequest/types-AgentMonitorRequest.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
