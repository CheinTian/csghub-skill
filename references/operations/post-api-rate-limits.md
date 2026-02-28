# POST /api_rate_limits

**Resource:** [ApiRateLimit](../resources/ApiRateLimit.md)
**Create a new api rate limit**
**Operation ID:** `post--api_rate_limits`

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.ApiRateLimitCreateRequest](../schemas/types-ApiRateLimitCreateRequest/types-ApiRateLimitCreateRequest.md)

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
