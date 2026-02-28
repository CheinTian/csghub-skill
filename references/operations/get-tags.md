# GET /tags

**Resource:** [Tag](../resources/Tag.md)
**Get all tags**
**Operation ID:** `get--tags`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `category` | query | string | No | category name |
| `scope` | query | enum: model, dataset, code... | No | scope name |
| `built_in` | query | boolean | No | built_in |
| `search` | query | string | No | search on name and show_name fields |

## Responses

| Status | Description |
|--------|-------------|
| 200 | tags |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
