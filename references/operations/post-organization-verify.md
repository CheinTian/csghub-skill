# POST /organization/verify

**Resource:** [OrganizationVerify](../resources/OrganizationVerify.md)
**Create organization verification**
**Operation ID:** `post--organization-verify`

create a new organization verification request

## Request Body

Organization verification request body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.OrgVerifyReq](../schemas/types-OrgVerifyReq/types-OrgVerifyReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
