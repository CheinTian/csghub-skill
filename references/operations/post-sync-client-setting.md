# POST /sync/client_setting

**Resource:** [Sync](../resources/Sync.md)
**Create sync client setting or update an existing sync client setting**
**Operation ID:** `post--sync-client_setting`

Create sync client setting or update an existing sync client setting, used for admin

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreateSyncClientSettingReq](../schemas/types-CreateSyncClientSettingReq/types-CreateSyncClientSettingReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
