# POST /spaces/{namespace}/{name}/stop

**Resource:** [Space](../resources/Space.md)
**stop space app**
**Operation ID:** `post--spaces-{namespace}-{name}-stop`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `current_user` | query | string | Yes | current_user |

## Responses

| Status | Description |
|--------|-------------|
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **JWT token**
