# POST /mirror/sources

**Resource:** [Mirror](../resources/Mirror.md)
**Create mirror source, used for admin**
**Operation ID:** `post--mirror-sources`

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreateMirrorSourceReq](../schemas/types-CreateMirrorSourceReq/types-CreateMirrorSourceReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
