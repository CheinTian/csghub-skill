# DELETE /agent/user-preferences

**Resource:** [Agent](../resources/Agent.md)
**Remove a preference for an entity (e.g., unpin)**
**Operation ID:** `delete--agent-user-preferences`

Remove a preference (e.g., unpin) for an entity.

## Request Body

Preference removal request

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
