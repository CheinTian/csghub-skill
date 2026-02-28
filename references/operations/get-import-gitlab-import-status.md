# GET /import/gitlab/import_status

**Resource:** [Import](../resources/Import.md)
**Import all gitlab repository**
**Operation ID:** `get--import-gitlab-import_status`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
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
