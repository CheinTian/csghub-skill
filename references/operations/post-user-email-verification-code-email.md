# POST /user/email-verification-code/{email}

**Resource:** [User](../resources/User.md)
**GenerateVerificationCodeAndSendEmail**
**Operation ID:** `post--user-email-verification-code-{email}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `email` | path | string | Yes | email |

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
