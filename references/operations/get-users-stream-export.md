# GET /users/stream-export

**Resource:** [User](../resources/User.md)
**Export users info. Only Admin**
**Operation ID:** `get--users-stream-export`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `verify_status` | query | string | No | Verify status (e.g. 'none', 'pending', 'approved', 'rejected') |
| `search` | query | string | No | Search keyword (match username/email/phone) |
| `labels` | query | string[] | No | Labels (e.g. vip,basic) - multiple values supported |
| `cursor` | query | integer (int64) | No | Cursor for pagination |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK - SSE stream: events are 'users' (single user JSON), 'error' (error message), 'end' (completion message) |
| 403 | Forbidden - not admin |

## Security

- **ApiKey**
