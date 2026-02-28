# PUT /licenses/import

**Resource:** [License](../resources/License.md)
**Import a license**
**Operation ID:** `put--licenses-import`

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
