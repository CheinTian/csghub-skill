# GET /datasets/{namespace}/{name}/dataviewer/catalog

**Resource:** [Dataset](../resources/Dataset.md)
**Get catalog of the dataset**
**Operation ID:** `get--datasets-{namespace}-{name}-dataviewer-catalog`

get catalog of the dataset

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |

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
