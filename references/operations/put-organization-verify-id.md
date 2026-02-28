# PUT /organization/verify/{id}

**Resource:** [OrganizationVerify](../resources/OrganizationVerify.md)
**Update organization verification**
**Operation ID:** `put--organization-verify-{id}`

update organization verification status (approved or rejected)

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | verification ID |

## Request Body

Update verification request body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.OrgVerifyStatusReq](../schemas/types-OrgVerifyStatusReq/types-OrgVerifyStatusReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
