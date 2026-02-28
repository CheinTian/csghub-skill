# POST /user/public/sms-code

**Resource:** [User](../resources/User.md)
**generate sms verification code and send it by sms (public endpoint)**
**Operation ID:** `post--user-public-sms-code`

generate sms verification code and send it by sms with scene parameter. Accessible to both logged-in and anonymous users.

## Request Body

SendPublicSMSCodeRequest

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.SendPublicSMSCodeRequest](../schemas/types-SendPublicSMSCodeRequest/types-SendPublicSMSCodeRequest.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
