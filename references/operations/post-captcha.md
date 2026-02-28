# POST /captcha

**Resource:** [Captcha](../resources/Captcha.md)
**Verify captcha**
**Operation ID:** `post--captcha`

verify captcha with user identity information

## Request Body

Captcha verification request

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CaptchaVerifyRequest](../schemas/types-CaptchaVerifyRequest/types-CaptchaVerifyRequest.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
