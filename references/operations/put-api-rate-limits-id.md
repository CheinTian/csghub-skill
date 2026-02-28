# PUT /api_rate_limits/{id}

**Resource:** [ApiRateLimit](../resources/ApiRateLimit.md)
**Update an api rate limit**
**Operation ID:** `put--api_rate_limits-{id}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | api rate limit ID |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.ApiRateLimitParam](../schemas/types-ApiRateLimitParam/types-ApiRateLimitParam.md)

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
