# GET /organization/{namespace}/notebooks

**Resource:** [Organization](../resources/Organization.md)
**Get organization notebooks**
**Operation ID:** `get--organization-{namespace}-notebooks`

get organization notebooks

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | org name |
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
