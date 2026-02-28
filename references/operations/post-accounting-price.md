# POST /accounting/price

**Resource:** [Accounting](../resources/Accounting.md)
**Add sku price**
**Operation ID:** `post--accounting-price`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `current_user` | query | string | Yes | current_user |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.AcctPriceCreateReq](../schemas/types-AcctPriceCreateReq/types-AcctPriceCreateReq.md)

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
