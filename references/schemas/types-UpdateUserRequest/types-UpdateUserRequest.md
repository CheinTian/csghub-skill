# types.UpdateUserRequest

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `avatar` | string | No |  |
| `bio` | string | No |  |
| `email` | string | No |  |
| `email_verification_code` | string | No |  |
| `homepage` | string | No |  |
| `name` | string | No | Display name of the user |
| `new_username` | string | No | if use want to change username, this should be the only field to send in request body |
| `phone` | string | No |  |
| `phone_area` | string | No |  |
| `roles` | string[] | No | should be updated by admin |
| `tag_ids` | integer[] | No |  |

