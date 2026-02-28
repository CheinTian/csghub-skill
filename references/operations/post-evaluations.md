# POST /evaluations

**Resource:** [Evaluation](../resources/Evaluation.md)
**run model evaluation**
**Operation ID:** `post--evaluations`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |

## Request Body

body setting of evaluation

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.EvaluationReq](../schemas/types-EvaluationReq/types-EvaluationReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
