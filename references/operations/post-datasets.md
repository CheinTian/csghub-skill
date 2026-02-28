# POST /datasets

**Resource:** [Dataset](../resources/Dataset.md)
**Create a new dataset**
**Operation ID:** `post--datasets`

create a new dataset

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `current_user` | query | string | No | current user, the owner |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreateDatasetReq](../schemas/types-CreateDatasetReq/types-CreateDatasetReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
