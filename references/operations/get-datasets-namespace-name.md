# GET /datasets/{namespace}/{name}

**Resource:** [Dataset](../resources/Dataset.md)
**Get dataset detail**
**Operation ID:** `get--datasets-{namespace}-{name}`

get dataset detail

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `current_user` | query | string | Yes | current_user |
| `need_op_weight` | query | boolean | No | need op weight |
| `need_multi_sync` | query | boolean | No | need multi sync |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
