# POST /accounting/recharge/{uuid}/create-pay-order

**Resource:** [Accounting](../resources/Accounting.md)
**Create recharge order for user or org**
**Operation ID:** `post--accounting-recharge-{uuid}-create-pay-order`

Create recharge order for user or org, the user uuid is the same as org uuid if it is org recharge

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `uuid` | path | string | Yes | recharge user or org uuid |

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
