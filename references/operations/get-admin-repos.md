# GET /admin/repos

**Resource:** [Repository](../resources/Repository.md)
**Get repo paths with search query**
**Operation ID:** `get--admin-repos`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `current_user` | query | string | No | current user name |
| `search` | query | string | Yes | search query |
| `type` | query | enum: model, dataset, code... | Yes | repository type query |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
