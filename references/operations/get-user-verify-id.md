# GET /user/verify/{id}

**Resource:** [UserVerify](../resources/UserVerify.md)
**Get user verification**
**Operation ID:** `get--user-verify-{id}`

get user verification information by user ID

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | user UUID |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
