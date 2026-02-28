# POST /mirror/batch

**Resource:** [Mirror](../resources/Mirror.md)
**Batch create mirrors**
**Operation ID:** `post--mirror-batch`

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.BatchCreateMirrorReq](../schemas/types-BatchCreateMirrorReq/types-BatchCreateMirrorReq.md)

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
