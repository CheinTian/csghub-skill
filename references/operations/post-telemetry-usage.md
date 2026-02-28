# POST /telemetry/usage

**Resource:** [Telemetry](../resources/Telemetry.md)
**Submit telemetry data for a client**
**Operation ID:** `post--telemetry-usage`

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [telemetry.Usage](../schemas/telemetry-Usage/telemetry-Usage.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

**Success Response Schema:**

[types.Response](../schemas/types-Response/types-Response.md)

## Security

- **ApiKey**
