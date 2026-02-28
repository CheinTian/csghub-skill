# GET /api_rate_limits/{id}

**Resource:** [ApiRateLimit](../resources/ApiRateLimit.md)
**Get an api rate limit by ID**
**Operation ID:** `get--api_rate_limits-{id}`

Get an api rate limit by ID from database

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | api rate limit ID |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 500 | Internal server error |

## Security

- **ApiKey**
