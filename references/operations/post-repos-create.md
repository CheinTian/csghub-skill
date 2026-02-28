# POST /repos/create

**Resource:** [Repository](../resources/Repository.md)
**Create a new repository, compatible with hf api**
**Operation ID:** `post--repos-create`

## Request Body

create repo request

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreateRepoReq](../schemas/types-CreateRepoReq/types-CreateRepoReq.md)

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
