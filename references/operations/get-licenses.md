# GET /licenses

**Resource:** [License](../resources/License.md)
**List license**
**Operation ID:** `get--licenses`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `product` | query | string | No | product |
| `edition` | query | string | No | edition |
| `search` | query | string | No | search |
| `current_user` | query | string | Yes | current user |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
