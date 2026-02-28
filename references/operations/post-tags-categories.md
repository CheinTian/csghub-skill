# POST /tags/categories

**Resource:** [Tag](../resources/Tag.md)
**Create new category**
**Operation ID:** `post--tags-categories`

Create new category, used for admin

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreateCategory](../schemas/types-CreateCategory/types-CreateCategory.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
