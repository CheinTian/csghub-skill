# GET /accounting/price/multi-kind

**Resource:** [Accounting](../resources/Accounting.md)
**List sku prices by multiple sku kinds**
**Operation ID:** `get--accounting-price-multi-kind`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `sku_type` | query | enum: 1, 2 | Yes | sku_type |
| `sku_kinds` | query | string[] | Yes | sku_kinds |
| `resource_id` | query | string | No | resource_id |
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
