# POST /accounting/recharge/create-pay-order

**Resource:** [Accounting](../resources/Accounting.md)
**Create recharge order**
**Operation ID:** `post--accounting-recharge-create-pay-order`

## Request Body

Recharge request payload

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.AcctRechargeReq](../schemas/types-AcctRechargeReq/types-AcctRechargeReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

**Success Response Schema:**

[types.AcctRechargeResp](../schemas/types-AcctRechargeResp/types-AcctRechargeResp.md)

## Security

- **ApiKey**
