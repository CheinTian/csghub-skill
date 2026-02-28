# GET /users/by-uuids

**Resource:** [User](../resources/User.md)
**Find users by UUIDs**
**Operation ID:** `get--users-by-uuids`

Retrieve a list of users by their UUIDs

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `uuids` | query | string[] | Yes | User UUIDs |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
