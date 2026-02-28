# POST /licenses/verify

**Resource:** [License](../resources/License.md)
**Verify a license**
**Operation ID:** `post--licenses-verify`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `current_user` | query | string | Yes | current user |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.ImportLicenseReq](../schemas/types-ImportLicenseReq/types-ImportLicenseReq.md)

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
