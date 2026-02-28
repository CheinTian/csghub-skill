# PUT /agent/instances/by-content-id/{type}/{content_id}

**Resource:** [Agent](../resources/Agent.md)
**Update an existing agent instance by type and content id**
**Operation ID:** `put--agent-instances-by-content-id-{type}-{content_id}`

Update the details of an existing agent instance by type and content id

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `type` | path | string | Yes | type |
| `content_id` | path | string | Yes | content id |

## Request Body

Updated instance data

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UpdateAgentInstanceRequest](../schemas/types-UpdateAgentInstanceRequest/types-UpdateAgentInstanceRequest.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 403 | Forbidden |
| 500 | Internal server error |

## Security

- **ApiKey**
