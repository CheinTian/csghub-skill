# POST /events

**Resource:** [Events](../resources/Events.md)
**Report client events**
**Operation ID:** `post--events`

## Request Body

Events

**Required:** Yes

**Content Types:** `application/json`

**Schema:** Array of [types.Event](../schemas/types-Event/types-Event.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

