# PUT /notifications/read

**Resource:** [Notifications](../resources/Notifications.md)
**Mark notifications as read**
**Operation ID:** `put--notifications-read`

Mark specified notifications or all notifications as read

## Request Body

Mark as read request

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
