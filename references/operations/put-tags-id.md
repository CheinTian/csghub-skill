# PUT /tags/{id}

**Resource:** [Tag](../resources/Tag.md)
**Update a tag by id**
**Operation ID:** `put--tags-{id}`

Update a tag by id, used for admin

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | id of the tag |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UpdateTag](../schemas/types-UpdateTag/types-UpdateTag.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
