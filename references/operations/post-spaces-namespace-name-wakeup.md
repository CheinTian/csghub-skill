# POST /spaces/{namespace}/{name}/wakeup

**Resource:** [Space](../resources/Space.md)
**wake up space app**
**Operation ID:** `post--spaces-{namespace}-{name}-wakeup`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |

## Responses

| Status | Description |
|--------|-------------|
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **JWT token**
