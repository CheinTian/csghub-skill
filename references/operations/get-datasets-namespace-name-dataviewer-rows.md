# GET /datasets/{namespace}/{name}/dataviewer/rows

**Resource:** [Dataset](../resources/Dataset.md)
**Get rows of the dataset**
**Operation ID:** `get--datasets-{namespace}-{name}-dataviewer-rows`

get rows of the dataset

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `config` | query | string | Yes | config |
| `split` | query | string | Yes | split |
| `search` | query | string | No | search |
| `where` | query | string | No | where |
| `orderby` | query | string | No | orderby |
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
