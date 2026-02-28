# POST /finetunes

**Resource:** [Finetune](../resources/Finetune.md)
**run fineune with model and dataset**
**Operation ID:** `post--finetunes`

## Request Body

body setting of finetune

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.FinetuneReq](../schemas/types-FinetuneReq/types-FinetuneReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
