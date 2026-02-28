# types.AgentMCPServerListItem

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `avatar` | string | No |  |
| `built_in` | boolean | No |  |
| `capabilities` | object | No |  |
| `created_at` | string | No |  |
| `description` | string | No |  |
| `id` | string | No | String ID (format: "builtin:{id}" or "user:{id}") |
| `installed` | boolean | No |  |
| `is_pinned` | boolean | No | Whether the MCP server is pinned by the user |
| `name` | string | No |  |
| `need_install` | boolean | No |  |
| `owner` | string | No |  |
| `protocol` | string | No |  |
| `status` | string | No | Connection status: 'connected'，'error' |
| `updated_at` | string | No |  |
| `url` | string | No |  |

