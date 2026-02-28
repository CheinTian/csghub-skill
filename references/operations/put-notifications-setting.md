# PUT /notifications/setting

**Resource:** [Notifications](../resources/Notifications.md)
**Update subscription settings**
**Operation ID:** `put--notifications-setting`

Update the user's notification settings

## Request Body

Update subscription request

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UpdateNotificationReq](../schemas/types-UpdateNotificationReq/types-UpdateNotificationReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 401 | Unauthorized |
| 500 | Internal server error |

## Security

- **ApiKey**
