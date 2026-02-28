# database.User

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `accessTokens` | database.AccessToken[] | No |  |
| `avatar` | string | No |  |
| `bio` | string | No |  |
| `can_change_username` | boolean | No | allow user to change username once |
| `company_verified` | boolean | No |  |
| `created_at` | string | No |  |
| `deletedAt` | string | No |  |
| `email` | string | No |  |
| `email_verified` | boolean | No |  |
| `gender` | string | No |  |
| `git_id` | integer | No |  |
| `homepage` | string | No |  |
| `id` | integer | No |  |
| `labels` | string[] | No |  |
| `last_login_at` | string | No |  |
| `name` | string | No |  |
| `namespace` | database.Namespace[] | No |  |
| `password_hash` | string | No | password for user registered without casdoor |
| `phone` | string | No |  |
| `phone_area` | string | No |  |
| `phone_verified` | boolean | No |  |
| `reg_provider` | string | No | user registered from default login page, from casdoor, etc. Possible values:

- "default"
- "casdoor" |
| `retain_data` | string | No |  |
| `role_mask` | string | No |  |
| `tags` | database.UserTag[] | No |  |
| `updated_at` | string | No |  |
| `username` | string | No |  |
| `uuid` | string | No | TODO:add unique index after migration |
| `verify_status` | object | No | none, pending, approved, rejected |

