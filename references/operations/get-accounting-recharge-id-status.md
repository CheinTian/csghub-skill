# GET /accounting/recharge/{id}/status

**Resource:** [Accounting](../resources/Accounting.md)
**Fetch recharge order status by recharge id**
**Operation ID:** `get--accounting-recharge-{id}-status`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | recharge uuid |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

**Success Response Schema:**

[types.RechargeStatusResp](../schemas/types-RechargeStatusResp/types-RechargeStatusResp.md)

## Security

- **ApiKey**
