# POST /codes

**Resource:** [Code](../resources/Code.md)
**Create a new code**
**Operation ID:** `post--codes`

create a new code

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `current_user` | query | string | No | current user, the owner |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreateCodeReq](../schemas/types-CreateCodeReq/types-CreateCodeReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
