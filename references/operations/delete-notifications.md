# DELETE /notifications

**Resource:** [Notifications](../resources/Notifications.md)
**Delete notification**
**Operation ID:** `delete--notifications`

Delete a notification

## Request Body

Delete notifications request

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
