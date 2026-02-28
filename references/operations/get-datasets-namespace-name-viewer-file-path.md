# GET /datasets/{namespace}/{name}/viewer/{file_path}

**Resource:** [Dataset](../resources/Dataset.md)
**Get the demo data of the dataset**
**Operation ID:** `get--datasets-{namespace}-{name}-viewer-{file_path}`

get the demo data of the dataset

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `file_path` | path | string | Yes | file_path |
| `per` | query | integer | No | per |
| `page` | query | integer | No | per page |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

**Success Response Schema:**

[types.Response](../schemas/types-Response/types-Response.md)

## Security

- **ApiKey**
