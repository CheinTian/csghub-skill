# GET /notebooks/{id}/logs/{instance}

**Resource:** [Notebook](../resources/Notebook.md)
**get notebook logs**
**Operation ID:** `get--notebooks-{id}-logs-{instance}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | notebook id |
| `instance` | path | string | Yes | notebook instance name |
| `since` | query | string | No | since time. Optional values: 10mins, 30mins, 1hour, 6hours, 1day, 2days, 1week |

## Responses

| Status | Description |
|--------|-------------|
| 400 | Bad request. May occur when the since time format is unsupported |
| 500 | Internal server error |

## Security

- **JWT token**
