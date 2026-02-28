# POST /mirror/repo

**Resource:** [Mirror](../resources/Mirror.md)
**Create mirror repo**
**Operation ID:** `post--mirror-repo`

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreateMirrorRepoReq](../schemas/types-CreateMirrorRepoReq/types-CreateMirrorRepoReq.md)

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
