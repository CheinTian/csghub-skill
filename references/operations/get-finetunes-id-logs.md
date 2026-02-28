# GET /finetunes/{id}/logs

**Resource:** [Finetune](../resources/Finetune.md)
**get finetune job logs**
**Operation ID:** `get--finetunes-{id}-logs`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | finetune job id |
| `since` | query | string | No | since time. Optional values: 10mins, 30mins, 1hour, 6hours, 1day, 2days, 1week |

## Responses

| Status | Description |
|--------|-------------|
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **JWT token**
