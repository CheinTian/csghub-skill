# PUT /accounting/price/{id}

**Resource:** [Accounting](../resources/Accounting.md)
**Update sku price**
**Operation ID:** `put--accounting-price-{id}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | id |
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
