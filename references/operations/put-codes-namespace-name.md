# PUT /codes/{namespace}/{name}

**Resource:** [Code](../resources/Code.md)
**Update a exists code**
**Operation ID:** `put--codes-{namespace}-{name}`

update a exists code

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

**Schema:** [types.UpdateCodeReq](../schemas/types-UpdateCodeReq/types-UpdateCodeReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
