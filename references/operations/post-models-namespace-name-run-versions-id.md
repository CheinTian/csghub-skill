# POST /models/{namespace}/{name}/run/versions/{id}

**Resource:** [Model](../resources/Model.md)
**create a new inference version**
**Operation ID:** `post--models-{namespace}-{name}-run-versions-{id}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `id` | path | integer | Yes | id |

## Request Body

req

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreateInferenceVersionReq](../schemas/types-CreateInferenceVersionReq/types-CreateInferenceVersionReq.md)

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
