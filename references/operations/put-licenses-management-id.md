# PUT /licenses/management/{id}

**Resource:** [License](../resources/License.md)
**Update a license by id**
**Operation ID:** `put--licenses-management-{id}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | id |
| `current_user` | query | string | Yes | current user |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UpdateLicenseReq](../schemas/types-UpdateLicenseReq/types-UpdateLicenseReq.md)

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
