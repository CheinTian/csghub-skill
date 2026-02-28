# GET /notifications/setting

**Resource:** [Notifications](../resources/Notifications.md)
**Get notification settings**
**Operation ID:** `get--notifications-setting`

get settings or default settings

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `timezone` | query | string | No | Timezone |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 401 | Unauthorized |
| 500 | Internal server error |

## Security

- **ApiKey**
