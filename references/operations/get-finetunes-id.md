# GET /finetunes/{id}

**Resource:** [Finetune](../resources/Finetune.md)
**get Finetune job by id**
**Operation ID:** `get--finetunes-{id}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | id |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

**Success Response Schema:**

[types.EvaluationRes](../schemas/types-EvaluationRes/types-EvaluationRes.md)

## Security

- **ApiKey**
