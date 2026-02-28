# types.ApiRateLimitCreateRequest

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `param` | object | Yes |  |
| `path` | string | Yes |  |

## Nested Fields

### `param`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `checkIP` | boolean | No |  |
| `limit` | integer | Yes |  |
| `window` | integer | No | in seconds |

