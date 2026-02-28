# PUT /notifications/unread

**Resource:** [Notifications](../resources/Notifications.md)
**Mark notifications as unread**
**Operation ID:** `put--notifications-unread`

Mark specified notifications or all notifications as unread

## Request Body

Mark as unread request

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.BatchNotificationOperationReq](../schemas/types-BatchNotificationOperationReq/types-BatchNotificationOperationReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 401 | Unauthorized |
| 500 | Internal server error |

## Security

- **ApiKey**
