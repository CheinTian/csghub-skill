# GET /mirrors

**Resource:** [Mirror](../resources/Mirror.md)
**Get mirrors, used for admin**
**Operation ID:** `get--mirrors`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `per` | query | integer | No | per |
| `page` | query | integer | No | page |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
