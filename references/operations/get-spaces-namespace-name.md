# GET /spaces/{namespace}/{name}

**Resource:** [Space](../resources/Space.md)
**show space detail**
**Operation ID:** `get--spaces-{namespace}-{name}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `current_user` | query | string | Yes | current_user |
| `need_op_weight` | query | boolean | No | need op weight |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
