# PUT /agent/templates/{id}

**Resource:** [Agent](../resources/Agent.md)
**Update an existing agent template**
**Operation ID:** `put--agent-templates-{id}`

Update the details of an existing agent template

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer (int64) | Yes | Template ID |

## Request Body

Updated template data

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.AgentTemplate](../schemas/types-AgentTemplate/types-AgentTemplate.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 403 | Forbidden |
| 500 | Internal server error |

## Security

- **ApiKey**
