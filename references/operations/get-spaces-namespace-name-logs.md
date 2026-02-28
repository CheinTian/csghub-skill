# GET /spaces/{namespace}/{name}/logs

**Resource:** [Space](../resources/Space.md)
**get space logs**
**Operation ID:** `get--spaces-{namespace}-{name}-logs`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `current_user` | query | string | Yes | current_user |
| `since` | query | string | No | since time. Optional values: 10mins, 30mins, 1hour, 6hours, 1day, 2days, 1week |

## Responses

| Status | Description |
|--------|-------------|
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **JWT token**
