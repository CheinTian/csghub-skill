# GET /{repo_type}/evaluations/{id}/cpu/{instance}/usage

**Resource:** [Monitor](../resources/Monitor.md)
**Get instance cpu usage for evaluation**
**Operation ID:** `get--{repo_type}-evaluations-{id}-cpu-{instance}-usage`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `repo_type` | path | enum: models | Yes | models |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
