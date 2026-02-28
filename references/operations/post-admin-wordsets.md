# POST /admin/wordsets

**Resource:** [Moderation](../resources/Moderation.md)
**Create sensitive word set**
**Operation ID:** `post--admin-wordsets`

## Request Body

Create sensitive word set

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreateSensitiveWordSetReq](../schemas/types-CreateSensitiveWordSetReq/types-CreateSensitiveWordSetReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

**Success Response Schema:**

[types.Response](../schemas/types-Response/types-Response.md)

