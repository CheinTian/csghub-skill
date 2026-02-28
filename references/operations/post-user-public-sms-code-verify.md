# POST /user/public/sms-code/verify

**Resource:** [User](../resources/User.md)
**verify sms verification code (public endpoint)**
**Operation ID:** `post--user-public-sms-code-verify`

verify sms verification code with scene parameter. Accessible to both logged-in and anonymous users.

## Request Body

VerifyPublicSMSCodeRequest

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.VerifyPublicSMSCodeRequest](../schemas/types-VerifyPublicSMSCodeRequest/types-VerifyPublicSMSCodeRequest.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
