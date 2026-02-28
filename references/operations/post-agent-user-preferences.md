# POST /agent/user-preferences

**Resource:** [Agent](../resources/Agent.md)
**Set a preference for an entity (e.g., pin)**
**Operation ID:** `post--agent-user-preferences`

Set a preference (e.g., pin) for an entity.

## Request Body

Preference request

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.AgentUserPreferenceRequest](../schemas/types-AgentUserPreferenceRequest/types-AgentUserPreferenceRequest.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 403 | Forbidden |
| 500 | Internal server error |

## Security

- **ApiKey**
