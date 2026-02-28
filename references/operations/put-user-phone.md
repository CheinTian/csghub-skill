# PUT /user/phone

**Resource:** [User](../resources/User.md)
**Update current user phone**
**Operation ID:** `put--user-phone`

## Request Body

UpdateUserPhoneRequest

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UpdateUserPhoneRequest](../schemas/types-UpdateUserPhoneRequest/types-UpdateUserPhoneRequest.md)

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
