# GET /collections

**Resource:** [Collection](../resources/Collection.md)
**get all collections**
**Operation ID:** `get--collections`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `search` | query | string | No | search text |
| `sort` | query | string | No | sort by |
| `per` | query | integer | No | per |
| `page` | query | integer | No | per page |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

