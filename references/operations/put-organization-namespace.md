# PUT /organization/{namespace}

**Resource:** [Organization](../resources/Organization.md)
**Update organization**
**Operation ID:** `put--organization-{namespace}`

update organization

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `current_user` | query | string | No | the op user |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.EditOrgReq](../schemas/types-EditOrgReq/types-EditOrgReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
