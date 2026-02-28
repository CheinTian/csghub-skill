# PUT /admin/wordsets/{id}

**Resource:** [Moderation](../resources/Moderation.md)
**Update sensitive word set**
**Operation ID:** `put--admin-wordsets-{id}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | Sensitive word set id |

## Request Body

Update sensitive word set

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UpdateSensitiveWordSetReq](../schemas/types-UpdateSensitiveWordSetReq/types-UpdateSensitiveWordSetReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

**Success Response Schema:**

[types.Response](../schemas/types-Response/types-Response.md)

