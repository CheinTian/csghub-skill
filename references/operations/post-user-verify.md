# POST /user/verify

**Resource:** [UserVerify](../resources/UserVerify.md)
**Create user verification**
**Operation ID:** `post--user-verify`

create a new user identity verification request

## Request Body

User verification request body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UserVerifyReq](../schemas/types-UserVerifyReq/types-UserVerifyReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
