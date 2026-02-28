# POST /user/{username}/ssh_keys

**Resource:** [SSH Key](../resources/SSH-Key.md)
**Create a new SSH key for the given user**
**Operation ID:** `post--user-{username}-ssh_keys`

create a new SSH key for the given user

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `username` | path | string | Yes | username |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreateSSHKeyRequest](../schemas/types-CreateSSHKeyRequest/types-CreateSSHKeyRequest.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
