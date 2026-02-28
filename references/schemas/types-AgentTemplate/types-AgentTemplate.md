# types.AgentTemplate

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `content` | string | No | Used to store the complete content of the template |
| `created_at` | string | No | When the template was created |
| `description` | string | No | Agent template description |
| `id` | integer | No |  |
| `is_pinned` | boolean | No | Whether the template is pinned by the user |
| `metadata` | object | No | Template metadata |
| `name` | string | Yes | Agent template name |
| `public` | boolean | No | Whether the template is public |
| `type` | string | Yes | Possible values: langflow, agno, code, etc. |
| `updated_at` | string | No | When the template was last updated |

