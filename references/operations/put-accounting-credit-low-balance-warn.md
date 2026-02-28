# PUT /accounting/credit/low-balance-warn

**Resource:** [Accounting](../resources/Accounting.md)
**Set low balance warning threshold**
**Operation ID:** `put--accounting-credit-low-balance-warn`

Set the low balance warning threshold for the current authenticated user.

## Request Body

LowBalanceWarn request body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.SetLowBalanceWarnReq](../schemas/types-SetLowBalanceWarnReq/types-SetLowBalanceWarnReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | Low balance warning successfully set |
| 400 | Bad request, invalid JSON format |
| 401 | Unauthorized, user not found |
| 500 | Internal server error |

**Success Response Schema:**

[types.Response](../schemas/types-Response/types-Response.md)

## Security

- **ApiKey**
