# POST /notifications

**Resource:** [Notifications](../resources/Notifications.md)
**Send a message**
**Operation ID:** `post--notifications`

## Request Body

post a message request

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.MessageRequest](../schemas/types-MessageRequest/types-MessageRequest.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 401 | Unauthorized |
| 500 | Internal server error |

## Security

- **ApiKey**
