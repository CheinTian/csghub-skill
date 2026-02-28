# PUT /tags/categories/id

**Resource:** [Tag](../resources/Tag.md)
**Create new category**
**Operation ID:** `put--tags-categories-id`

Create new category, used for admin

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UpdateCategory](../schemas/types-UpdateCategory/types-UpdateCategory.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
