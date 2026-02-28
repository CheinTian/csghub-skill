# POST /user/sms-code

**Resource:** [User](../resources/User.md)
**generate sms verification code and send it by sms**
**Operation ID:** `post--user-sms-code`

## Request Body

SendSMSCodeRequest

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.SendSMSCodeRequest](../schemas/types-SendSMSCodeRequest/types-SendSMSCodeRequest.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
