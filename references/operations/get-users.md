# GET /users

**Resource:** [User](../resources/User.md)
**Get users info. Only Admin**
**Operation ID:** `get--users`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `verify_status` | query | string | Yes | verify_status |
| `search` | query | string | Yes | search |
| `labels` | query | string[] | No | labels, such as ['vip', 'basic'] |
| `exact_match` | query | boolean | No | exact_match, default is false |
| `exact_match` | query | boolean | No | exact_match, default is false |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
