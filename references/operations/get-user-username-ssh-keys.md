# GET /user/{username}/ssh_keys

**Resource:** [SSH Key](../resources/SSH-Key.md)
**Get all SSH keys for the given user**
**Operation ID:** `get--user-{username}-ssh_keys`

get all SSH keys for the given user

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `username` | path | string | Yes | username |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
