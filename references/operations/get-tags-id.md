# GET /tags/{id}

**Resource:** [Tag](../resources/Tag.md)
**Get a tag by id**
**Operation ID:** `get--tags-{id}`

Get a tag by id, used for admin

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | id of the tag |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
