# PUT /models/{namespace}/{name}

**Resource:** [Model](../resources/Model.md)
**Update a exists model**
**Operation ID:** `put--models-{namespace}-{name}`

update a exists model

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `current_user` | query | string | No | current user, the model owner |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UpdateModelReq](../schemas/types-UpdateModelReq/types-UpdateModelReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
