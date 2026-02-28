# GET /sync/version/latest

**Resource:** [Sync](../resources/Sync.md)
**Get latest version**
**Operation ID:** `get--sync-version-latest`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `cur` | query | string | Yes | current version |
| `current_user` | query | string | Yes | current_user |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
