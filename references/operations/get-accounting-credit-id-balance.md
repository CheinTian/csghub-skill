# GET /accounting/credit/{id}/balance

**Resource:** [Accounting](../resources/Accounting.md)
**Get user balance by user uuid**
**Operation ID:** `get--accounting-credit-{id}-balance`

Get user balance by user uuid, used for admin or current user

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | user uuid |
| `current_user` | query | string | Yes | current_user |

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
