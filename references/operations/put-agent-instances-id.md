# PUT /agent/instances/{id}

**Resource:** [Agent](../resources/Agent.md)
**Update an existing agent instance**
**Operation ID:** `put--agent-instances-{id}`

Update the details of an existing agent instance

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer (int64) | Yes | Instance ID |

## Request Body

Updated instance data

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.AgentInstance](../schemas/types-AgentInstance/types-AgentInstance.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 403 | Forbidden |
| 500 | Internal server error |

## Security

- **ApiKey**
