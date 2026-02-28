# PUT /datasets/{namespace}/{name}

**Resource:** [Dataset](../resources/Dataset.md)
**Update a exists dataset**
**Operation ID:** `put--datasets-{namespace}-{name}`

update a exists dataset

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `current_user` | query | string | No | current user, the owner |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UpdateDatasetReq](../schemas/types-UpdateDatasetReq/types-UpdateDatasetReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
