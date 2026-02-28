# POST /validate-yaml

**Resource:** [Repository](../resources/Repository.md)
**Validate yaml, compatible with hf api**
**Operation ID:** `post--validate-yaml`

## Request Body

validate yaml content

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.ValidateYamlReq](../schemas/types-ValidateYamlReq/types-ValidateYamlReq.md)

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
