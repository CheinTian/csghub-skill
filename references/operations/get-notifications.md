# GET /notifications

**Resource:** [Notifications](../resources/Notifications.md)
**List notifications**
**Operation ID:** `get--notifications`

List all notifications with pagination and filtering options

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `page` | query | integer | No | Page number |
| `page_size` | query | integer | No | Number of items per page |
| `notification_type` | query | string | No | Type of notification |
| `unread_only` | query | boolean | No | Only return unread notifications |
| `title` | query | string | No | Notification title |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 401 | Unauthorized |
| 500 | Internal server error |

## Security

- **ApiKey**
