# PUT /accounting/credit/{id}/recharge

**Resource:** [Accounting](../resources/Accounting.md)
**Recharge fee for account**
**Operation ID:** `put--accounting-credit-{id}-recharge`

Recharge fee for account, used for admin

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | user uuid |
| `current_user` | query | string | Yes | current_user |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.RechargeReq](../schemas/types-RechargeReq/types-RechargeReq.md)

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
