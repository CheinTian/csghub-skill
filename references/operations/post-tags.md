# POST /tags

**Resource:** [Tag](../resources/Tag.md)
**Create new tag**
**Operation ID:** `post--tags`

Create new tag, used for admin

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreateTag](../schemas/types-CreateTag/types-CreateTag.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
