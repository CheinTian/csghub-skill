# types.AgentInstance

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `built_in` | boolean | No | Whether the instance is built-in |
| `content_id` | string | No | Used to specify the unique id of the instance resource |
| `created_at` | string | No | When the instance was created |
| `description` | string | No | Instance description |
| `editable` | boolean | No | Whether the instance is editable |
| `id` | integer | No |  |
| `is_pinned` | boolean | No | Whether the instance is pinned by the user |
| `is_running` | boolean | No | Whether the instance is running |
| `metadata` | object | No | Instance metadata |
| `name` | string | No | Instance name |
| `public` | boolean | No | Whether the instance is public |
| `template_id` | integer | No | Associated with the id in the template table |
| `type` | string | No | Possible values: langflow, agno, code, etc. |
| `updated_at` | string | No | When the instance was last updated |

