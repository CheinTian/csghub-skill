# GET /organization/{namespace}/codes

**Resource:** [Organization](../resources/Organization.md)
**Get organization codes**
**Operation ID:** `get--organization-{namespace}-codes`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | org name |
| `current_user` | query | string | Yes | current user name |
| `per` | query | integer | No | page size |
| `page` | query | integer | No | current page number |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
