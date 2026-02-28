# database.Organization

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `created_at` | string | No |  |
| `description` | string | No |  |
| `git_path` | string | No |  |
| `homepage` | string | No |  |
| `id` | integer | No |  |
| `logo` | string | No |  |
| `name` | string | No |  |
| `namespace` | [database.Namespace](database-Namespace.md) | No |  |
| `namespace_id` | integer | No |  |
| `org_type` | string | No |  |
| `path` | string | No | unique name of the organization |
| `updated_at` | string | No |  |
| `user` | [database.User](database-User.md) | No |  |
| `user_id` | integer | No |  |
| `uuid` | string | No |  |
| `verified` | boolean | No |  |
| `verify_status` | object | No | none, pending, approved, rejected |

