# PUT /user/verify/{id}

**Resource:** [UserVerify](../resources/UserVerify.md)
**Update user verification**
**Operation ID:** `put--user-verify-{id}`

update user verification status (approved or rejected)

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer (int64) | Yes | verification ID |

## Request Body

Update verification request body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UserVerifyStatusReq](../schemas/types-UserVerifyStatusReq/types-UserVerifyStatusReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
