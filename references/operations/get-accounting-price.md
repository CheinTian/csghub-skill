# GET /accounting/price

**Resource:** [Accounting](../resources/Accounting.md)
**List sku prices**
**Operation ID:** `get--accounting-price`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `sku_type` | query | enum: 1, 2 | Yes | sku_type |
| `sku_kind` | query | string | Yes | sku_kind |
| `resource_id` | query | string | Yes | resource_id |
| `current_user` | query | string | Yes | current_user |
| `per` | query | integer | No | per |
| `page` | query | integer | No | per page |

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
