# POST /import/gitlab/import

**Resource:** [Import](../resources/Import.md)
**Import gitlab repository, used for admin**
**Operation ID:** `post--import-gitlab-import`

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.ImportReq](../schemas/types-ImportReq/types-ImportReq.md)

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
