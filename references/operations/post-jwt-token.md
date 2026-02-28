# POST /jwt/token

**Resource:** [JWT](../resources/JWT.md)
**generate jwt token for user**
**Operation ID:** `post--jwt-token`

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreateJWTReq](../schemas/types-CreateJWTReq/types-CreateJWTReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

**Success Response Schema:**

[types.CreateJWTResp](../schemas/types-CreateJWTResp/types-CreateJWTResp.md)

## Security

- **ApiKey**
