# DELETE /licenses/{id}

**Resource:** [License](../resources/License.md)
**Delete a license by id**
**Operation ID:** `delete--licenses-{id}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | id |
| `current_user` | query | string | Yes | current user |

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
