# GET /notifications/poll/{limit}

**Resource:** [Notifications](../resources/Notifications.md)
**Poll new notifications**
**Operation ID:** `get--notifications-poll-{limit}`

Poll new notifications with a specified limit

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `limit` | path | integer | Yes | The maximum number of new notifications to poll |
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
