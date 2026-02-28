# POST /organizations

**Resource:** [Organization](../resources/Organization.md)
**Create a new organization**
**Operation ID:** `post--organizations`

create a new organization

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `current_user` | query | string | No | the op user |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreateOrgReq](../schemas/types-CreateOrgReq/types-CreateOrgReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
