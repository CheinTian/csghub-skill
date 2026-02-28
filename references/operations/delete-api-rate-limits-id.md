# DELETE /api_rate_limits/{id}

**Resource:** [ApiRateLimit](../resources/ApiRateLimit.md)
**Delete an api rate limit**
**Operation ID:** `delete--api_rate_limits-{id}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | api rate limit ID |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 500 | Internal server error |

**Success Response Schema:**

[types.Response](../schemas/types-Response/types-Response.md)

## Security

- **ApiKey**
