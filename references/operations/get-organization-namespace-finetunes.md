# GET /organization/{namespace}/finetunes

**Resource:** [Organization](../resources/Organization.md)
**Get organization finetune jobs**
**Operation ID:** `get--organization-{namespace}-finetunes`

get organization finetune jobs

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
