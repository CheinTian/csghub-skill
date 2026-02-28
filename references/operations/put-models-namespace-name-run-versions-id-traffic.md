# PUT /models/{namespace}/{name}/run/versions/{id}/traffic

**Resource:** [Model](../resources/Model.md)
**update inference version traffic percent**
**Operation ID:** `put--models-{namespace}-{name}-run-versions-{id}-traffic`

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

**Schema:** Array of [types.UpdateInferenceVersionTrafficReq](../schemas/types-UpdateInferenceVersionTrafficReq/types-UpdateInferenceVersionTrafficReq.md)

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
