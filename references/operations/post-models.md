# POST /models

**Resource:** [Model](../resources/Model.md)
**Create a new model**
**Operation ID:** `post--models`

create a new model

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `current_user` | query | string | No | current user |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreateModelReq](../schemas/types-CreateModelReq/types-CreateModelReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
