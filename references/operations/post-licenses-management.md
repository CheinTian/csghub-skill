# POST /licenses/management

**Resource:** [License](../resources/License.md)
**Create a license**
**Operation ID:** `post--licenses-management`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `current_user` | query | string | Yes | current user |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreateLicenseReq](../schemas/types-CreateLicenseReq/types-CreateLicenseReq.md)

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
