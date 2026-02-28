# GET /import/gitlab

**Resource:** [Import](../resources/Import.md)
**Import all gitlab repository**
**Operation ID:** `get--import-gitlab`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `base_url` | query | string | Yes | gitlab instance url |
| `access_token` | query | string | Yes | gitlab instance access token |
| `search` | query | string | No | search query |
| `per` | query | integer | No | per |
| `page` | query | integer | No | per page |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
