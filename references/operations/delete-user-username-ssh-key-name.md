# DELETE /user/{username}/ssh_key/{name}

**Resource:** [SSH Key](../resources/SSH-Key.md)
**Delete specific SSH key for the given user**
**Operation ID:** `delete--user-{username}-ssh_key-{name}`

delete specific SSH key for the given user

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `username` | path | string | Yes | username |
| `name` | path | string | Yes | key name |

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
